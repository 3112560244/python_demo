import requests
from bs4 import BeautifulSoup
import wordcloud
import jieba

if __name__ == "__main__":
    # UA 伪装
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    # URL
    url = "https://www.xygwh.cc/44/44462/"

    # 请求命令
    page_text = requests.get(url=url, headers=header)
    page_text.encoding = "gbk"
    page_text = page_text.text
    soup = BeautifulSoup(page_text, "html.parser")

    # bs4 解析
    li_list = soup.select("body > div.listmain > dl > dd")

    for li in li_list:
        #print(li)
        title = li.a.text
        new_url = "https://www.xygwh.cc"+li.a["href"]

        # 新的请求命令
        response = requests.get(url=new_url, headers=header)
        response.encoding = "gbk"
        new_page_text = response.text
        new_soup = BeautifulSoup(new_page_text, "html.parser")

        page = new_soup.find("div", class_="showtxt").text

        with open("雪中悍刀行.txt", "a", encoding="utf-8") as fp:
            fp.write("\n" + title + ":" + "\n" + "\n" + page)

        print(title + "下载完成！！！")


    with open("雪中悍刀行.txt", "r", encoding='utf-8') as file:
        txt = file.read()

    words = jieba.lcut(txt)

    for i in range(len(words)):
        if len(words[i])<=1:
            words[i]=''

    w = wordcloud.WordCloud(font_path='msyh.ttc')
    w.generate(" ".join(words))
    w.to_file("雪中悍刀行.png")
