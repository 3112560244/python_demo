# 定义商品信息
products = {
    "苹果": 1.5,
    "香蕉": 1,
    "橘子": 1,
    "火龙果": 4,
    "柚子": 5,
}

# 定义用户余额
balance = 10

# 定义购物清单
shopping_cart = []


# 定义购买商品的函数
def buy_product(product, quantity):
    global balance
    # 计算总价
    total_price = products[product] * quantity
    # 判断余额是否足够
    if total_price > balance:
        print("余额不足")
        print("当前余额: ${:.2f}".format(balance))
        return
    # 更新余额
    balance -= total_price
    # 添加商品到购物车
    shopping_cart.append((product, quantity, total_price))
    print("成功购买 {} {} for ${:.2f}.".format(quantity, product, total_price))
    print("当前余额: ${:.2f}".format(balance))


# 定义菜单
def menu():
    print("{0:>15}".format("购物系统商品列表"))
    print("{0:>5}{1:>10}".format("产品名称", "产品价格(元/斤)"))
    for key, value in products.items():
        print("{0:>5}{1:>10}".format(key, value))


if __name__ == '__main__':
    # 循环flag
    flag = True

    # 菜单输出
    menu()
    while flag:
        product = input("请输入购买物品名称，退出请输入结束")
        if product == '结束':
            break
        if not product in products.keys():
            print("请输入正确的商品名称")
            continue
        quantity = float(input("请输入购买数量，退出请输入结束"))
        if quantity == '结束':
            break
        buy_product(product, quantity)

    # 输出购物车信息
    print("购物车:")
    for item in shopping_cart:
        print("- {} {} for ${:.2f}".format(item[1], item[0], item[2]))
    print("当前余额: ${:.2f}".format(balance))
