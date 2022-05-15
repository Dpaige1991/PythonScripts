import turtle
import time

turtle.setup(600, 600, 0, 276)
turtle.bgcolor("black")

leo = turtle.Turtle()
leo.pensize(10)
leo.speed(1)
leo.ht()

colors = ["red",
          "yellow",
          "blue",
          "green",
          "orange",
          "purple",
          "magenta",
          "deepskyblue"]

# i = 0
def wheel():
    leo.pencolor(colors[i])
    leo.up()
    leo.bk(40)
    leo.rt(90)
    leo.down()
    leo.circle(40, 180)
    leo.pencolor(colors[(i + 1) % 8])
    leo.circle(40, 180)
    leo.up()
    leo.lt(90)
    leo.fd(40)
    leo.down()


for i in range(8):
    wheel()


turtle.mainloop()
