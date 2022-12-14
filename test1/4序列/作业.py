#写一个用户登录程序，把多个用户的用户名和密码信息事先保存到列表当中，当用户登录时，首先判断用户名是否存在，如果不存在，就要求用户重新输入用户名（最多给3次机会）；如果用户名存在，就继续判断密码是否正确，如果正确，就提示登录成功，如果密码错误，就提示重新输入密码（最多给3次机会）。

users = [['qx','123456'],['lyr','123456']]
users_dict = dict(users)
names = list(users_dict.keys())
print(names)
tag = 1
while tag :
    name = str(input('请输入用户名'))
    if names.count(name):
        pwd = str(input('请输入密码'))
        if users_dict.get(name) == pwd:
            print('登陆成功')
            break
    print('用户名或密码错误请重新输入')