

#
# l = [54, 36, 75, 28, 50]
# l.append(42)
# print(l)
# l.insert(l.index(28), 66)
# print(l)
# print(l[4])
# l.remove(28)
# l.sort(reverse=True)
# print(l)
# l.clear()
# print(l)
#
# list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_1.append("abc")
# print(list_1)
# list_1.extend(['e', 'f', 'g'])
# print(list_1)
# list_1.remove(3)
# list_1.remove(4)
# list_1.remove(5)
# print(list_1)
# list_1.insert(0, 's')
# print(list_1)
# list_1[list_1.index(0)] = 'hello'
# print(list_1)
#
# nums = [3, 6, 10, 14, 2, 7]
# list_num = []
# for i in range(0, len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == 9:
#             list_num.append((nums[i], nums[j]))
# print(list_num)
#
#
#
#
# sum1 = int(input('请输入评委人数'))
# list_num = []
# for i in range(0, sum1):
#     list_num.append(float(input('请打分')))
# list_num.sort()
# del list_num[0]
# del list_num[-1]
# print(sum(list_num) / len(list_num))


# none = 1
# nums = []
# while none:
#     s = input("请输入奇数个整数 空格隔开")
#     slist = s.split(' ')
#     print(slist)
#     for i in range(0, len(slist)):
#         nums.append(int(slist[i]))
#     if len(nums)%2==1:
#         none = 0
#     else:
#         continue;
# print(nums)
# nums.sort()
# print(nums[len(nums)//2])

# x = float(input("请输入一个数字"))
# o = input("请输入运算符号")
# y = float(input("请输入第二个数字"))
# if o == '+':
#     print(x + y)
# elif o == '-':
#     print(x - y)
# elif o == '*':
#     print(x * y)
# elif o == '/':
#     if y == 0:
#         print("除数不能为0")
#     else:
#         print(x / y)
# else:
#     print("运算符号输入有误")


#
# lss=[['张三',18,'郑州市'],['李四',19,'开封市'],['王五',20,'洛阳市'],['赵六',18,'许昌市']]
#
# for i in range(0,4):
#     del lss[i][1]
#
# for i in range(0,4):
#     print(lss[i])


s = input().split()
L = int(s[0])
M = int(s[1])
arr = []
for i in range(L + 1):
    arr.append(True)
for i in range(M):
    s = input().split()
    for j in range(int(s[0]), int(s[1]) + 1):
        arr[j] = False
counter = 0
for i in range(L + 1):
    if arr[i] == True:
        counter += 1
print(counter)


#
# lst_1=[10, 10, 6, 10,10, 2, 10,10,10, 4, 10, 3, 10, 8, 10, 2, 10, 3, 10,10]
# for i in range(0,lst_1.count(10)):
#     lst_1.remove(10)
# print(lst_1)
