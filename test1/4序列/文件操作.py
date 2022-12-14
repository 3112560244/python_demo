# with open("test.txt","r") as file:
#     a = file.read(1)
#     print(a)
#     print("*"*30)
#     b = file.read()
#     print(b)


# with open("test.txt", "r") as file:
#     a = file.readline()
#     print(a)


# with open("test.txt", "r") as file:
#     for a in file:
#         print(a)

# with open("test.txt", "r") as file1,open("text2.txt","w") as file2:
#     file2.write(file1.read())


# with open('test.txt','r',encoding="UTF-8") as fp:
#     data = fp.readlines()
#
# data = [int(line.strip()) for line in data]
# data.sort()
# data = [str(i) + '\n' for i in data]
# with open('test2.txt','w+') as fp:
#     fp.writelines(data)


# 文件目录操作
import os

a = os.getcwd()
print(a)

os.mkdir("ostest")
os.chdir('ostest')
os.mkdir('mktest')
f = open('1.txt','w')
