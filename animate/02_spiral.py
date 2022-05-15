import turtle  # 导入 turtle 库(工具包)
import time

"""窗口设置"""
turtle.setup(600, 600, 0, 275)
turtle.bgcolor("black")

"""画笔设置"""
leo = turtle.Turtle()
leo.pensize(20)
leo.pencolor("white")
leo.speed(0)
leo.ht()

'''开始绘图'''
i = 0

def spiral():
    for i in range(360):
        # leo.pensize(10 + i / 24)
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
