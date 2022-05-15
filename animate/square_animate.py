import turtle as t
import time

t.setup(600, 600, 0, 275)
t.bgcolor("black")

p = t.Turtle()
p.pensize(10)
p.speed(0)
p.ht()

colors = ['red', 'yellow', 'blue', 'green']


def square():
    for i in range(4):
        p.pencolor(colors[i])
        p.fd(200)
        p.rt(90)

number = 0
degree = 1

try:
    while True:
        t.tracer(0)
        p.clear()
        
        p.up()
        p.home()
        p.lt(135 + degree * number)
        p.fd(141)
        p.rt(135)
        p.down()
        
        square()
        number += 1
        
        t.update()
        time.sleep(0.01)
except:
    print("Exit")
