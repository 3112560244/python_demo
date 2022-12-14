# list_test = [1,2,3]
#
# print(len(list_test))
#
# num_list  = list(range(1,5))
# print(num_list)
#
# num_list = list(range(1,10,2))
# print(num_list)
# print(num_list[4])
#
# for num in num_list:
#     print(num)
#
# num_list.append(11)
# num_list.insert(1,10)
#
# num_list.extend(list_test)
# print(num_list.count(1))
#
# print(num_list.index(7))
#
# print('数组值和:',sum(num_list))
#
# num_list.pop()
# print(num_list)
#
# num_list.remove(1)
# print(num_list)
#
#
# num_list.sort()
# print('升序排序后的数组',num_list)
#
# num_list.sort(reverse=True)
# print('降序排序后的数组',num_list)
#
# print(id(num_list))
# list_copy = sorted(num_list)
# print(num_list)
# print(list_copy)
# print(id(list_copy))
#
#
#
# num_list = num_list +[999]
# print(num_list)
#
# print('999在数组里吗',999 in num_list)
#
# a_range = range(10)
# a_list = [x*x for x in a_range]
# print(a_list)


names = []
names.append('Xiaoming')
names.append('Panpan')
names.append('Dongdong')
print(names)

names.insert(2,'Yueyue')
print(names)

names[3]='东东'
print(names)

names.insert(1,['Mingming','Xiaoyun'])
print(names)


print(names.index('Panpan'))

nums = [1,2,3,4,5]
names.extend(nums)
print(names)

print(names[3:7])

print(names[2:9:2])

print(names[-1:-5:-1])
print(names[-4:])


for name in names:
    print(names.index(name),name)

print(type(names))