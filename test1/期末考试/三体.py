import jieba
import requests
from bs4 import BeautifulSoup
import wordcloud



def writeBook():
    # UA 伪装
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.90 Safari/537.36 "
    }
    # URL
    url = "https://www.shizongzui.cc/santi/"

    # 请求命令
    page_text = requests.get(url=url, headers=header)
    page_text.encoding = "utf-8"
    page_text = page_text.text
    soup = BeautifulSoup(page_text, "html.parser")

    # bs4 解析
    li_list = soup.select("body > div.booklist.clearfix > span")

    for li in li_list:
        if len(li.contents) == 1:
            title = li.contents[0]
            print(title)
            with open("../网络请求/三体.txt", "a", encoding="utf-8") as fp:
                fp.write("\n" + "\n" + title + ":" + "\n")
        else:
            title = li.contents[1].contents[0]
            new_url = li.a['href']
            # 新的请求命令
            response = requests.get(url=new_url, headers=header)
            response.encoding = "utf-8"
            new_page_text = response.text
            new_soup = BeautifulSoup(new_page_text, "html.parser")

            page = new_soup.find("div", id="BookText").text

            with open("三体三部全.txt", "a", encoding="utf-8") as fp:
                fp.write("\n" + "\n" + title + ":" + "\n" + page)

        print(title + "下载完成！！！")


def readBook():
    with open('三体三部全.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    # 将文本分词
    # list = jieba.lcut(text, cut_all=False)
    lists = jieba.lcut(text)

    # 统计词频
    word_freq = {}
    for word in lists:
        if (
                word == '一个' or word == '没有' or word == '他们' or word == '我们' or word == '这个' or word == '自己' or word == '已经' or word == 'pla' or word == 'way'):
            continue
        if (len(word) == 1):
            continue
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # items = list(word_freq.items())
    # items.sort(key=lambda x: x[1], reverse=True)
    # for i in range(20):
    #     word, count = items[i]
    #     print("{0:<10}{1:>5}".format(word, count))

    # 生成词云
    w = wordcloud.WordCloud(font_path='msyh.ttc',
                            background_color='white',
                            width=800,
                            height=600).generate_from_frequencies(word_freq)

    w.generate(" ".join(word_freq))
    w.to_file("三体.png")


if __name__ == "__main__":
    # 抓取三体三部曲 写入文件
    writeBook()

    # 读取三体 生成词云
    readBook()
