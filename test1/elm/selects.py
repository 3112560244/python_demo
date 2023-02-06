import http.client
import json
import pushplus
import requests

def getCookie1():

    url = "https://elm.139201.xyz/bales/chdd.php"

    querystring = {"t": "1675658208", "i": "E3zmXL"}

    payload = ""
    headers = {
        "Host": "elm.139201.xyz",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    # 获取cookie
    cookie = response.cookies.get_dict()
    print(cookie, type(cookie))

    dic_str = json.loads(str(cookie).replace("'", "\""))
    PHPSESSID = dic_str["PHPSESSID"]
    # print(PHPSESSID)
    return PHPSESSID

def getCookie():
    url = "https://l.139201.xyz/l/?E3zmXL "


    headers = {
        # "Host": "l.139201.xyz",
        # "Upgrade-Insecure-Requests": "1",
        # "Accept-Language": "zh-CN,zh;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",

    }

    response = requests.request("GET", url,  headers=headers)

    # 获取cookie
    cookie = response.cookies.get_dict()
    print(cookie, type(cookie))

    dic_str = json.loads(str(cookie).replace("'", "\""))
    PHPSESSID = dic_str["PHPSESSID"]
    # print(PHPSESSID)
    return PHPSESSID

def getInfo(selectPhone):
    # PHPSESSID = getCookie()
    # print(PHPSESSID)
    conn = http.client.HTTPSConnection("elm.139201.xyz")

    payload = "command=&action=next21&phone="+selectPhone+"&location=&locationInfo="
    # payload = "phone=17739510180"


    headers = {
        # 'cookie': "PHPSESSID="+"gihq4hd88cvbqn0m0fbghak2v2",
        'cookie': "PHPSESSID="+"gihq4hd88cvbqn0m0fbghak2v2",

        # 'cookie': "PHPSESSID=" + PHPSESSID,
        'Host': "elm.139201.xyz",
        # 'Connection': "keep-alive",
        # 'Content-Length': "64",
        # 'Accept': "*/*",
        # 'X-Requested-With': "XMLHttpRequest",

        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4374 MMWEBSDK/20221206 Mobile Safari/537.36 MMWEBID/1601 MicroMessenger/8.0.32.2300(0x28002034) WeChat/arm32 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",

    }

    conn.request("POST", "/bales/waimai_api.php", payload, headers)

    res = conn.getresponse()
    data = res.read()
    t = data.decode("utf-8")

    d = json.loads(t)

    if d['status'] != 1:
        print(d['message'])
    else:
        data = d['data']
        accountInfo = data['accountInfo']
        html = ""

        isLoginChd = data['isLoginChd']
        isLogin = data['isLogin']
        phone = data['phone']

        # 账户资产
        peaCount = accountInfo['peaCount']
        balance = accountInfo['balance']
        expireCount = accountInfo['expireCount']
        # 月获得
        plusCount = accountInfo['plusCount']

        # return "手机号: "+phone+"</br>"+"登陆状态: "+isLogin +"</br>"


        # 今日收获
        chd_number = data['chd_number']
        money = data['money']
        # 昨日收获
        chd_number_yesterday = data['chd_number_yesterday']
        money_yesterday = data['money_yesterday']
        # 累积获得
        bean_total = data['bean_total']


        # 剩余天数
        chd_surplus = data['chd_surplus']
        balance_surplus = data['balance_surplus']

        html = '<div  style="color: #333;font-size: 17px;z-index：999;"><div style="position: absolute; right: 0; padding: 10px 20px; font-size: 35px; color: #0085ff;" onclick="cl();"></div><div style="padding:16px 5px 10px 5px;text-align:center;font-weight: bold;"><p style="margin-bottom: 5px;">当前查询账号：' + phone + '</p>';
        # html = '<div class="layui-m-layercont" style="color: #333;font-size: 17px;z-index：999;"><div style="position: absolute; right: 0; padding: 10px 20px; font-size: 35px; color: #0085ff;" onclick="cl();">×</div><div style="padding:16px 5px 10px 5px;text-align:center;font-weight: bold;"><p style="margin-bottom: 5px;">当前查询账号：' + phone + '</p>';
        html += '<p style="margin-bottom: 3px;font-size: 14px;">总吃货豆：' + str(peaCount) + '&nbsp;&nbsp;&nbsp;总余额：' + str(balance) + '&nbsp;&nbsp;&nbsp;将过期吃货豆：' + str(expireCount) + '  </p>';

        html +='<p style="margin-bottom: 2px;">【吃货豆】状态：'+ '在线' if isLoginChd else '离线' + '  </p>';
        html += '<p style="margin-bottom: 2px;">今日获得(晚上为准)：' + chd_number + '</p>';
        html += '<p style="margin-bottom: 2px;">昨日获得：' + chd_number_yesterday + '</p>';
        html += '<p style="margin-bottom: 2px;">累计获得：' + data['bean_total'] + '</p>';

        html += '<p style="margin-bottom: 8px;">吃豆累计在线/剩余天数：' + str(data['online_total_day']) + '/' + str(data['chd_surplus']) + '天</p>';

        html += '<p style="margin-bottom: 2px;">【刷余额】状态：'+'在线' if data['isLoginYe'] else '离线' + '  </p>';
        html += '<p style="margin-bottom: 2px;">今日获得：' + str(data['money']) + '</p>';
        html += '<p style="margin-bottom: 2px;">昨日获得：' + str(data['money_yesterday']) + '</p>';
        html += '<p style="margin-bottom: 2px;">累计获得：' + str(data['money_total']) + '</p>';
        html += '<p style="margin-bottom: 8px;">余额累计在线/剩余天数：' + str(data['balance_online_total_day']) + '/' + str(data['balance_surplus']) + '天</p>';

    return html

phone = '13140110864'
phone = '17739510180'

html = getInfo(phone)

pushplus.push("豆豆通知", html)

