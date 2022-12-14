def index1():
    try:
        sum = int(input("请输入学生成绩"))
        if 0<=sum<=100 :
            print("学生的成绩是",sum)
        else:
            print("请输入[0，100]")

    except BaseException:
        print("请输入整数")


def devide(x,y):
    try:
        return int(x)/int(y)
    except ZeroDivisionError:
        return 'division by zero！'
    except ValueError:
        return '数据类型错误' 

x = input('请输入被除数')
y = input('请输入除数')
print(devide(x,y))