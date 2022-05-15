import turtle
import time

turtle.setup(600, 600, 0, 276)
turtle.bgcolor("black")

leo = turtle.Turtle()
leo.pensize(3)
leo.speed(0)
leo.ht()

colors = ["red",
          "yellow",
          "blue",
          "purple",
          "orange",
          "green"]


def eight_side():
    for i in range(6):
        leo.color('white')
        leo.fd(200)
        leo.rt(120)
        leo.color(colors[i])
        leo.fd(200)
        leo.rt(120)
        leo.color('white')
        leo.fd(200)
        leo.rt(120)
        leo.rt(60)


leo.dot(20, 'white')
try:
    while True:
        turtle.tracer(0, 1)
        leo.clear()
        leo.rt(1)
        eight_side()
        turtle.update()
        time.sleep(0.01)
except:
    print("Exit")
