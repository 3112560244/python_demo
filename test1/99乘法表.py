# # 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('{}x{}={}\t'.format(j, i, j * i), end='')
#     print()
#
# # 水仙花数
# exit_flag = False
# num = 0;
# for i in range(1, 9):
#     for j in range(0, 9):
#         for k in range(0, 9):
#             num = k + 10 * j + 100 * i
#             if num == i ** 3 + j ** 3 + k ** 3:
#                 exit_flag = True
#             if exit_flag:
#                 break
#         if exit_flag:
#             break
#     if exit_flag:
#         break
# print("第一个三位数水仙花数为:", num)
#
# # 计算从0-100所有奇数的合
# num = 0
# for i in range(0, 101):
#     if i >= 100:
#         break
#     if i % 2 == 1:
#         num += i
#
# print(num)
#
# # 计算0-9中的偶数
# for i in range(1, 10):
#     if i % 2 == 0:
#         print(i, end=' ')
#     else:
#         pass


# 圆周率的计算
# from random import random
#
# n = 10000
# N = 0
# for i in range(1, n + 1):
#     x, y = random(), random()
#     dis = pow(x ** 2 + y ** 2, 0.5)
#     if dis <= 1:
#         N = N + 1
# print(4*N / n)


# 斐波那契数列
# i,j = 0,1
# while i <10000:
#     print(i)
#     i,j = j,i+j

# 求出100~200之间的所有素数
# import math
#
# for i in (100,201):
#     prime = 1
#     k = int(math.sqrt(i))
#     for n in range(2,k+1):
#         if(i%n==0):
#             prime =0
#             break
#     if prime==0:
#         print(i)

# import math
# i = 0
# for n in range(100,201):
#     prime = 1
#     k = int(math.sqrt(n)) # sqrt(n)方法返回数字n的平方根
#     for i in range(2,k+1):
#         if n % i == 0:
#             prime = 0
#     if prime ==1:
#         print("%d是素数" % n)

# 找出15个 1 2 3 4 组成的各位不相同的三位数
# sum = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         if i == j:
#             continue
#         for k in range(1, 5):
#             if k == i | k == j:
#                 continue
#             sum = sum + 1
#             print(100 * i + 10 * j + k)
#             if sum == 15:
#                 break
#         if sum == 15:
#             break
#     if sum == 15:
#         break

# 猜随机数 1-1000
# from random import random
# sys_num = int(random() * 1000 + 1)

import random
sys_num = random.randint(1, 1001)
user_num = 0
print(sys_num)
while user_num != sys_num:
    user_num = int(input("请输入1-1000"))
    if user_num > sys_num:
        print('猜大了')
    elif user_num < sys_num:
        print('猜小了')
    else:
        print('恭喜你中奖了')
