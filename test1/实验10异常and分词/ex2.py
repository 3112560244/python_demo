import jieba


# 全模式
def num1(text):
    list1 = jieba.cut(text,cut_all=True)
    print('全模式')
    for word in list1:
        print(word,' ' ,end="")

# 精确模式
def num2(text):
    list2 = jieba.cut(text,cut_all=False)
    print('精确模式')
    for word in list2:
        print(word,' ' ,end="")

# 搜索引擎模式
def num3(text):
    list3 = jieba.cut_for_search(text)
    print('搜索引擎模式')
    for word in list3:
        print(word,' ' ,end="")

with open("郑州财经学院信息工程学院新闻.txt","r",encoding='utf-8') as file:
    text = file.read()

num1(text)
num2(text)
num3(text)
