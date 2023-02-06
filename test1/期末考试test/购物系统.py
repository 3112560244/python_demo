menus = {
    "葡萄": 6.5,
    "榴莲": 38,
    "橘子": 1.7,
    "火龙果": 4.7,
    "甘蔗": 4.7,
}

money = 100

lists = []


def buy(product, quantity):
    global money

    total_price = menus[product] * quantity

    if total_price > money:
        print("余额不足")
        print("当前余额: ${:.2f}".format(money))
        return

    money -= total_price

    lists.append((product, quantity, total_price))
    print("成功购买 {} {} {}".format(quantity, product,total_price))
    print("余额: {:.2f}".format(money))


# 菜单
def menu():
    print("产品名称", "产品价格")
    for key, value in menus.items():
        print("{0:>5}{1:>5}".format(key, value))


if __name__ == '__main__':
    # 循环flag
    flag = True

    # 菜单输出
    menu()
    while flag:
        product = input("请输入购买物品名称，退出请输入结束")
        if product == '结束':
            break
        if not product in menus.keys():
            print("请输入正确的商品名称")
            continue
        quantity = float(input("请输入购买数量，退出请输入结束"))
        if quantity == '结束':
            break
        buy(product, quantity)

    # 输出购物车信息
    print("购物车:")
    for item in lists:
        print("{} {} {}".format(item[1], item[0],item[2]))
    print("当前余额: {:.2f}".format(money))
