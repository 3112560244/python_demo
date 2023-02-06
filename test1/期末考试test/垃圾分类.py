waste_dict = {
    "可回收垃圾": ["报刊", "塑料袋", "纸箱"],
    "有害垃圾": ["电池", "水银温度计", "过期药品"],
    "厨余垃圾": ["骨头", "剩饭", "果皮"],
    "其他垃圾": ["烟头", "渣土", "卫生间废纸"], }
while True:
    search_waste = input("请输入您要查询的垃圾：")
    find = False
    if search_waste == "退出":
        break
    for classify, waste in waste_dict.items():
        if search_waste in waste:
            find = True
            print(f"{search_waste}的类别是：{classify}")
            print("-" * 30)
    if find == False:
        print("对不起，没有找到该垃圾的分类，请自行判断。")
        print("-" * 30)
        for calssiyf, waste in waste_dict.items():
            print(f"{classify}包括：", end="")
            for item in waste:
                if waste.index(item) == len(waste) - 1:
                    print(item)
                else:
                    print(item, end=",")
        print("-" * 30)
while True:
    option = input("您是否希望将此垃圾加入到现有的分类中呢?(Y/N)")
    if option == "Y":
        classify = input("您希望将垃圾加入到哪个类别？")
        try:
            waste_dict[classift].append(search_waste)
        except KeyError:
            print("您输入的有误，没有该类别。")
        break
    elif option == "N":
        print("您可以继续查询垃圾分类")
        break
    else:
        print("您的输入有误，请重新输入：")
