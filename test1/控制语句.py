# a, b, c = 4, 5, 0
# if a > b:
#     c = a
# if b > a:
#     c = b
# print("两个数的最大值为", c)
#
# if a % 2 == 0:
#     print("偶数")
# else:
#     print("奇数")

import math

m = int(input("请输入一个数"))
n = int(math.sqrt(m))
prime = 1
for i in range(2, n+1):
    if m % i == 0:
        prime = 0
    else:
        prime = 1
if prime ==1:
    print("是素数")
else:
    print('不是素数')

