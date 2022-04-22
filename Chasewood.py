from turtle import *
turtle = Turtle()
screen = Screen()
screen.bgcolor("black")
turtle.speed(1)
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()
pensize(5)
turtle.pencolor("magenta")
for i in range(4):
  turtle.forward(100)
  turtle.left(90)
mainloop()
