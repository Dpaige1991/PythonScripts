import turtle
import time

w_width = 600
w_height = 600
turtle.setup(w_width, w_height, 838, 46)
turtle.bgcolor("#2E5B84")
# turtle.bgpic("images/logo_600.png")

leo = turtle.Turtle()
leo.pencolor('yellow')
leo.speed(0)


def pen_goto(x, y):
    leo.up()
    leo.goto(x, y)
    leo.down()


s = 25
x = - w_width / 2
y = w_height / 2
loop_time = int(w_height / s + 1)


def ref_line():
    turtle.tracer(0)
    for i in range(loop_time):
        pen_goto(x, (y - 25 * i))
        leo.fd(w_width)
    leo.rt(90)
    for i in range(loop_time):
        pen_goto((x + 25 * i), y)
        leo.fd(w_width)
    leo.up()
    leo.home()
    leo.down()
    turtle.tracer(1)


def face_1():
    leo.color('white')
    leo.begin_fill()
    pen_goto(200, -300)
    leo.circle(100, 90)
    leo.fd(400)
    pen_goto(300, 200)
    leo.circle(100, 90)
    leo.fd(400)
    pen_goto(-200, 300)
    leo.circle(100, 90)
    leo.fd(400)
    pen_goto(-300, -200)
    leo.circle(100, 90)
    leo.fd(400)
    leo.end_fill()


def face_2():
    leo.color('black')
    pen_goto(-300, 212)
    leo.begin_fill()
    for i in range(2):
        leo.fd(600)
        leo.right(90)
        leo.fd(324)
        leo.right(90)
    leo.end_fill()


def square():
    leo.begin_fill()
    for i in range(4):
        leo.fd(24)
        leo.rt(90)
    leo.end_fill()


def left_eye():
    leo.color("#6EEDFC")
    for i in range(3):
        pen_goto(-205 + 31 * i, 115)
        square()
    leo.color("#66DDF6")
    for i in range(5):
        pen_goto(-236 + 31 * i, 84)
        square()
    leo.color("#54B9E5")
    for i in range(5):
        pen_goto(-236 + 31 * i, 53)
        square()
    leo.color("#3880CD")
    for i in range(5):
        pen_goto(-236 + 31 * i, 22)
        square()
    leo.color("#2459BD")
    for i in range(3):
        pen_goto(-205 + 31 * i, -9)
        square()


def right_eye():
    leo.color("#6EEDFC")
    for i in range(3):
        pen_goto(119 + 31 * i, 115)
        square()
    leo.color("#66DDF6")
    for i in range(5):
        pen_goto(88 + 31 * i, 84)
        square()
    leo.color("#54B9E5")
    for i in range(5):
        pen_goto(88 + 31 * i, 53)
        square()
    leo.color("#3880CD")
    for i in range(5):
        pen_goto(88 + 31 * i, 22)
        square()
    leo.color("#2459BD")
    for i in range(3):
        pen_goto(119 + 31 * i, -9)
        square()


def magikid():
    # leo.color("#505050")
    pen_goto(0, -208)
    # leo.write("MAGIKID", font=("Nasalization", 78, "normal"))
    turtle.addshape("images/magikid.gif")
    leo.shape("images/magikid.gif")


def blink_close():
    turtle.tracer(0)
    leo.color("black")
    for i in range(3):
        pen_goto(119 + 31 * i, 115)
        square()
    for i in range(3):
        pen_goto(119 + 31 * i, -9)
        square()
    time.sleep(0.3)
    for i in range(5):
        pen_goto(88 + 31 * i, 84)
        square()
    for i in range(5):
        pen_goto(88 + 31 * i, 22)
        square()
    turtle.tracer(1)

def blink_open():
    turtle.tracer(0)
    leo.color("#6EEDFC")
    for i in range(3):
        pen_goto(119 + 31 * i, 115)
        square()
    leo.color("#2459BD")
    for i in range(3):
        pen_goto(119 + 31 * i, -9)
        square()
    time.sleep(0.3)
    leo.color("#66DDF6")
    for i in range(5):
        pen_goto(88 + 31 * i, 84)
        square()
    leo.color("#3880CD")
    for i in range(5):
        pen_goto(88 + 31 * i, 22)
        square()
    turtle.tracer(1)


# ref_line()
face_1()
face_2()
left_eye()
right_eye()
time.sleep(1)
for i in range(2):
    blink_close()
    time.sleep(0.3)
    blink_open()
    time.sleep(0.5)
time.sleep(0.5)
magikid()
time.sleep(0.5)
leo.clear()
turtle.bgpic("images/logo_600.png")
leo.ht()
time.sleep(1)
turtle.tracer(0)
face_2()
left_eye()
right_eye()
for i in range(2):
    blink_close()
    time.sleep(0.3)
    blink_open()
    time.sleep(0.5)

turtle.mainloop()
