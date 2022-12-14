import requests				#导入requests库
from bs4 import BeautifulSoup		#导入BeautifulSoup


def getHtml(url):
    #异常处理
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        r = requests.get(url,headers=headers)
        r.raise_for_status()			#如果状态不是200，则引发异常
        r.encoding = 'utf-8'			#更改编码方式
        return r.text				#返回页面内容
    except:
        return "异常"				#发生异常返回空字符

def allhtml(html):
    bsObj = BeautifulSoup(html, "html.parser")	
    divList = bsObj.find('div',class_='mtop pages').text
    divList = str(divList)
    sum = int(divList.split('条')[0]);

    print("新闻总数: ",sum,"共计页数: ",sum//30+1)


    html1 = "http://jsj.zzife.edu.cn/29582/"
    getcon(html,1)

    # 如果存在分页 处理其他分页
    if int(sum)>30 :

        for i in range(2,(sum//30+2)):
            html2 = html1+"list-"+str(i)+".html"
            html3 = getHtml(html2)
            getcon(html3,i)


def getcon(html,index):
    bsObj = BeautifulSoup(html, "html.parser")	
    divList = bsObj.find('ul',class_='adaplist103').find_all('li')

    allnew = []
    for divs in divList:
        text = divs.find('a')['title']
        allnew.append(text)

    # 输出新闻
    print("\n"+"--第: "+str(index)+" 页新闻--"+"\n")
    for new in allnew:
        print(new)
    
    # 写入文件
    write(allnew,index)


def write(allnew,index):
    with open("./郑州财经学院信息工程学院新闻.txt", "a", encoding="utf-8") as fp:
        fp.write("\n" + "第: "+str(index)+" 页新闻" + "\n" + "\n")
        for new in allnew:
            fp.write(new+"\n")
        print("第: ",index," 页新闻下载完成！！！")




html = getHtml("http://jsj.zzife.edu.cn/29582/")	

# 获取所有分页页面
allhtml(html)

# 写入文件
