import jieba

with open('comment.txt', 'r', encoding='utf-8') as file:
    text = file.read()

lists = jieba.lcut(text)

words = {}
for word in lists:
    if (len(word) == 1):
        continue
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

items = list(words.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))

