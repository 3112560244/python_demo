import jieba

with open("三国演义.txt","r",encoding='utf-8') as file:
    txt = file.read()

words = jieba.lcut(txt)
counts = {}

for word in words:
    if(len(word) == 1):
        continue

    elif(word=='孔明曰'):
        word = '孔明'
    if(word=='玄德曰'):
        word = '玄德'
        
    counts[word] = counts.get(word,0)+1  #不在counts中返回0 

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse = True)
for i in range(15):
    word ,count= items[i]
    print("{0:<10}{1:>5}".format(word,count))