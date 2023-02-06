dicts = {"可回收垃圾": ["啤酒瓶", "饮料瓶", "纸"], "有害垃圾": ["电池", "杀虫剂", "药品"], "厨余垃圾": ["蔬菜皮", "剩菜", "剩饭"],
         "其他垃圾": ["毛发", "卫生间用纸", "瓷器碎片"]}


def laji():
    print("{0:>20}".format("请输入垃圾名称,输入结束退出"))
    name = input()
    if name == "结束":
        return False

    flag = False
    for key, value in dicts.items():
        for n in value:
            if (n == name):
                print("您输入的垃圾属于：",key)
                flag = True
    if flag:
        return flag

    print("您输入的垃圾暂时没有录入，请您在以下分类自行判断")
    for key,value in dicts.items():
        print(key,end="  ")
    return flag

if __name__ == '__main__':
    flag = True
    while flag:
        flag = laji()
