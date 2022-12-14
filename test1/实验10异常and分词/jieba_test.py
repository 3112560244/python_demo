import jieba


text = '在 python 中，当你导入一个库时，它应该在代码块中使用。因此，正如它显然指出的那样，您可能已经导入了这些但没有使用所有它们。'
words = jieba.cut(text)
counts = {}

for word in words:
    if len (word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0)+1

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse = True)

for i in range(3):
    word,count = items[i]
    print("{0:<4}{1:>4}".format(word,count))
