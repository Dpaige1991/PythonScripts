# * * * * * * * * * * * * * * * * * #
# 登陆 'magikid.com' 查看更多课程.     #
# 下载'程序源代码'及配套'课程资源',      #
# 完成'课后练习'还可获得'老师点评'.      #
# * * * * * * * * * * * * * * * * * #

import turtle

turtle.setup(600, 600, 0, 276)
turtle.bgcolor("black")

leo = turtle.Turtle()
leo.shape("turtle")
leo.pensize(1)
leo.color("cyan")
leo.speed(0)
leo.up()
leo.goto(30, 120)
leo.down()
leo.ht()

c = 0
d = 0

while True:
    turtle.tracer(6)
    for i in range(4):
        leo.forward(80)
        leo.right(90)
    leo.right(15)
    c += 1
    if c >= 24 + 2:
        leo.forward(60)
        c = 0
        d += 1
        if d >= 24 / 2:
            break

turtle.mainloop()
