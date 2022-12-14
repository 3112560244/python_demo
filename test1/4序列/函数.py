# def num1(n):
#     lt = []
#     i = 0
#     while i < n:
#         if i == 0 or i == 1:
#             lt.append(i)
#
#         else:
#             a = lt[i - 1] + lt[i - 2]
#             lt.append(a)
#
#         i += 1
#     return lt
#
# print(num1(10))

# def maopao(n):
#     for j in range(0, len(n)-1):
#         for i in range(0,len(n)-j-1):
#             if(n[i]>n[i+1]):
#                 max = n[i]
#                 n[i] = n[i+1]
#                 n[i+1] = max
#     return n
#
# print(maopao([1,3,9,5,2]))


# def avgScore(n):
#     sum = 0
#     for i in iter(n):
#         sum+=i
#     return sum/float(len(n))
#
# print(avgScore([1,2,3,4,6]))

#
# def num4(a,b,c):
#     if(a+b>c & a+c>b & b+c>a):
#         return "true"
#     return "false"
#
# print(num4(1,2,3))

from numbers import Number


# def isodd(x):
#     if x%1!=0:
#        return '不是整数'
#     if x%2!=0:
#         return 'true'
#     else:
#         return 'false'
#
# print(isodd(2))


# def change(str1):
#     str = []
#     for i in iter(str1):
#         if i>='a' and i <='z':
#             str.append(chr(ord(i)-32))
#         elif i>='A' and i <='Z':
#             str.append(chr(ord(i)+32))
#         else:
#             str.append(i)
#     return str
#
# print(''.join(change('ABCdef666')) )


# def gcd(a, b):
#     return gcd(b, a % b) if a % b else b
#
#
# def lcm(a, b):
#     return a * b // gcd(a, b)

# def gcd(a, b):
#     max1 = max(a,b)
#     min1 = min(a,b)
#     a = 1
#     while max1 % min1 != 0:
#         a = max1 % min1
#         max1 = min1
#         min1 = a
#     return min1
#
# def lcm(a, b):
#     return a * b // gcd(a, b)
#
# print(gcd(12, 4))
# print(lcm(15, 7))


# def num8():
#     a = -1
#     sum = 0
#     for i in range(1,100):
#         sum += (a ** (i - 1)) * (i ** 2)
#     return sum
#
# print(num8())


def num9(*a):
    sum = 0
    for i in iter(a):
        sum+=i
    return sum/float(len(a))

print(num9(1,2,3,4,6))
