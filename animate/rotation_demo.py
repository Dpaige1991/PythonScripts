import turtle
import time

turtle.setup(600, 600, 0, 275)
turtle.bgcolor("black")

leo = turtle.Turtle()
leo.pensize(10)
leo.speed(0)
leo.ht()

colors = ["red", "yellow", "blue", "green"]


def square():
    for i in range(4):
        leo.pencolor(colors[i])  # index
        leo.fd(200)
        leo.rt(90)


def pen_goto(x, y):
    leo.up()
    leo.goto(x, y)
    leo.down()


pen_goto(-100, 100)
square()

turtle.mainloop()
