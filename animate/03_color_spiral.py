import turtle  # 导入 turtle 库(工具包)
import time
import random

"""窗口设置"""
turtle.setup(600, 600)
turtle.bgcolor("black")
turtle.colormode(255)

"""画笔设置"""
leo = turtle.Turtle()
leo.pensize(20)
leo.pencolor(255, 255, 255)
leo.speed(0)
leo.ht()

'''开始绘图'''
i = 0
def spiral():
    for i in range(360):
        # leo.pensize(10 + i / 24)
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        leo.pencolor(a, b, c)
        leo.forward(0.2 * i)
        leo.right(10)

spiral()

while True:
    i += 1
    turtle.tracer(0, 0)
    leo.up()
    leo.home()
    leo.left(6 * i)
    leo.down()
    spiral()
    turtle.update()
    leo.clear()
    time.sleep(0.01)
    

turtle.done()
