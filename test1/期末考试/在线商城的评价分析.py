import jieba

def pingjia():
    with open('comment.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # 将文本分词
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

    items = list(word_freq.items())
    items.sort(key=lambda x: x[1], reverse=True)

    for i in range(15):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))


if __name__ == '__main__':
    pingjia()
