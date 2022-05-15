import turtle
import time

turtle.setup(600, 600, 0, 275)
turtle.bgcolor("black")
turtle.bgpic("images/demo1.png")

leo = turtle.Turtle()
leo.pensize(10)
leo.speed(0)
leo.ht()

colors = ["red",
          "yellow",
          "blue",
          "green",
          "red",
          "yellow",
          "blue",
          "green"]


def hexagon():
    for i in range(6):
        leo.pencolor(colors[i])
        leo.fd(200)
        leo.rt(360 / 6)


def trun():
    leo.up()
    leo.home()
    leo.left(120 + degree * number)
    leo.fd(200)
    leo.right(120)
    leo.down()


degree = -1
number = 0

try:
    while True:
        turtle.tracer(0)
        leo.clear()

        trun()
        hexagon()
        number += 1

        turtle.update()
        time.sleep(0.01)
except:
    print("Exit")

# turtle.mainloop()
