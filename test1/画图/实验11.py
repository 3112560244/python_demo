import turtle
import jieba
import wordcloud

def num1():
    turtle.setup(500, 500)
    for i in range(1, 5):
        turtle.circle(20 * i)


def num2():
    turtle.setup(500, 500)
    for i in range(1, 6):
        turtle.penup()
        turtle.goto(0, -20 * i)
        turtle.pendown()
        turtle.circle(20 * i)


def num3():
    turtle.screensize(bg="black")
    turtle.pencolor("yellow")
    turtle.fillcolor("white")
    turtle.setup(500, 500)

    turtle.begin_fill()
    for i in range(5):
        turtle.forward(200)
        turtle.right(144)
    turtle.end_fill()

def num4():
    with open("../实验10异常and分词/三国演义.txt", "r", encoding='utf-8') as file:
        txt = file.read()
    words = jieba.lcut(txt)

    for i in range(len(words)):
        if len(words[i])<=1:
            words[i]=''
        elif words[i] == '却说':
            words[i] = ''
        elif words[i] == '不可':
            words[i] = ''
        elif words[i] == '二人':
            words[i] = ''
        elif words[i] == '不能':
            words[i] = ''
        if(words[i] == '孔明曰'):
            words[i] = '孔明'
        elif (words[i] == '玄德曰'):
            words[i] = '玄德'

    w = wordcloud.WordCloud(font_path='msyh.ttc')
    w.generate(" ".join(words))
    w.to_file("三国演义.png")

num4()
turtle.done()
