import turtle
import time

# turtle.setup(800, 800)
turtle.bgpic("images/bg3.png")

leo = turtle.Turtle()
leo.pensize(10)
leo.speed(0)
leo.ht()

'''
leo.shape("circle")
leo.pencolor("red")
leo.up()
leo.goto(158, 75)
leo.down()
'''

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


leo.up()
leo.goto(158, 75)
leo.down()
hexagon()

number = 0

try:
    while True:
        turtle.tracer(0)
        leo.clear()

        leo.rt(1)
        hexagon()
        number += 1

        turtle.update()
        time.sleep(0.01)
except:
    print("Exit")

turtle.mainloop()
