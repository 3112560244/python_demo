dict_student = []


def menu():
    print('===========================学生信息管理系统=========================')
    print('-------------------------------功能菜单--------------------------------')
    print('\t\t\t\t\t\t\t1、录入学生信息')
    print('\t\t\t\t\t\t\t2、查找学生信息')
    print('\t\t\t\t\t\t\t3、删除学生信息')
    print('\t\t\t\t\t\t\t4、显示所有学生信息')
    print('\t\t\t\t\t\t\t5、保存信息到文件')
    print('\t\t\t\t\t\t\t6、通过文件恢复数据')
    print('\t\t\t\t\t\t\t0、退出')
    print('-------------------------------------------------------------------------')


def add():
    name = input("请输入姓名")
    num = input("请输入学号")
    sex = input("请输入性别")
    score = input("请输入成绩")
    student = {'id': num, 'name': name, 'sex': sex, 'score': score}
    dict_student.append(student)
    print("添加成功")


def select():
    stu = {}

    num = input("请输入学号")
    for student in dict_student:
        if student['id'] == num:
            stu = student
    if len(stu) != 0:
        print(stu)
    else:
        print("没有找到")


def delete():
    global dict_student
    old = dict_student
    new = []

    num = input("请输入学号")

    for student in old:
        if str(student['id']) != num:
            new.append(student)
    dict_student = new
    print("删除成功")


def list():
    global dict_student
    for student in dict_student:
        print(student)



def save():
    global dict_student
    students = ''
    for i in dict_student:
        students = students + str(i) + '\n'
    with open("student.txt", 'w', encoding='utf-8') as file:
        file.truncate()
        file.write(str(students))
    print("保存成功")


def load():
    global dict_student
    with open("student.txt", 'r', encoding='utf-8') as file:
        students = file.readlines()
        for item in students:
            dict_student.append(eval(item))
    print(dict_student)


def main():
    b = True
    while b:
        menu()
        num = int(input("请输入序号："))
        if num == 1:
            add()
        elif num == 2:
            select()
        elif num == 3:
            delete()
        elif num == 4:
            list()
        elif num == 5:
            save()
        elif num == 6:
            load()
        elif num == 0:
            b = False
        else:
            print("请重新输入")


if __name__ == '__main__':
    main()
