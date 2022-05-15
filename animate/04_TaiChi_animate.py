from turtle import *
import time


def pen_goto(a, b):  # 无痕移动画笔
    up()
    goto(a, b)
    down()


def coordinate_system():  # 绘制坐标轴和参考线
    row_y = 300
    for i in range(int(600 / 100 - 1)):
        row_y -= 100
        pen_goto(-300, row_y)
        fd(600)

    setheading(-90)

    column_x = -300
    for i in range(int(600 / 100 - 1)):
        column_x += 100
        pen_goto(column_x, 300)
        fd(600)

    setheading(0)


# -----------以下开始绘画-----------

def TaiChi():
    speed(10)
    # 一个完整的圆,分两次画
    color("black")
    begin_fill()
    circle(200, 180)
    end_fill()

    color("black", "white")
    begin_fill()
    circle(200, 180)
    end_fill()

    # 下面的半圆
    color("black")
    begin_fill()
    circle(100, -180)
    end_fill()

    # 上面的半圆
    color("white")
    begin_fill()
    circle(-100, -180)
    end_fill()

    # 上面的小圆
    up()
    rt(90)
    fd(120)
    lt(90)
    down()
    color("black")
    begin_fill()
    circle(20)
    end_fill()

    # 下面的小圆
    up()
    rt(90)
    fd(200)
    lt(90)
    down()
    color("white")
    begin_fill()
    circle(20)
    end_fill()


def main():
    setup(600, 600)
    up()
    home()
    rt(90)
    fd(200)
    lt(90)
    down()
    TaiChi()  # 调用绘制太极图的函数
    ht()
    time.sleep(1)
    i = 0
    while True:
        i += 1
        # if i > 360:
            # i -= 360
        tracer(0, 0)
        up()
        home()
        rt(90+6*i)
        fd(200)
        lt(90)
        down()
        TaiChi()
        update()
        clear()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
    mainloop()
