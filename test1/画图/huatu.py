import turtle

# turtle.setup(100, 100, 10, 10)

turtle.left(45)
turtle.fd(150)
turtle.right(135)
turtle.fd(300)
turtle.left(145)
turtle.fd(150)


turtle.fillcolor('white')
# 左画圆
turtle.circle(100)

# 右画圆  90度
turtle.circle(-100, 90)

turtle.mainloop()
