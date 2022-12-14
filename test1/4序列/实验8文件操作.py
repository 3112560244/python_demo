import os


def t1(path):
    lsdir = os.listdir(path)
    print("path:" + path)
    for dir in lsdir:
        if os.path.isdir(os.path.join(path, "\\\\" + dir)):
            t1(os.path.join(path + dir))
        else:
            print(os.getcwd() + "-" + dir)


def t2():
    os.chdir('ostest')
    with open("t2.txt", 'w', encoding='utf-8') as file:
        file.write("欢迎学习Python程序设计")


def t4():
    os.chdir('ostest')
    sum = 0
    with open('t4.txt', 'r') as file:
        f = str(file.read())
        print(f)
        list = f.split()
        for num in list:
            sum += int(num)
        print(sum / len(list))


def t5():
    os.chdir('ostest')
    sum = 0
    with open('data2.txt', 'r') as file:
        f = str(file.read())
        list = f.split(',')
        nums = []
        print(list)
        for num in list:
            nums.append(int(num))
        for num1 in range(len(nums)-1):
           for num2 in range(num1+1,len(nums)):
               print(num1,num2)
               if nums[num1]<nums[num2]:
                    sum = nums[num1]
                    nums[num1] = nums[num2]
                    nums[num2] = sum
           print(nums)
        print("desc:",nums)


if __name__ == '__main__':
    # t1('E:\编程\Python\\' + 'test\\test1')
    t2()
    # t4()
    # t5()
