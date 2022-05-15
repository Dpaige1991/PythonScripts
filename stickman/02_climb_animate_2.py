import tkinter as tk
import time

root = tk.Tk()
cv_width = 1280
cv_height = 720
cv = tk.Canvas(root, width=cv_width, height=cv_height, bg='black')
cv.pack()

climb_up = [
    tk.PhotoImage(file="images/climb300/climb_up_1.png"),
    tk.PhotoImage(file="images/climb300/climb_up_2.png"),
    tk.PhotoImage(file="images/climb300/climb_up_3.png"),
    tk.PhotoImage(file="images/climb300/climb_up_4.png")
]
stickman_climb = cv.create_image(cv_width / 2, cv_height / 2, image=climb_up[0])

'''创建动画变量'''
image_index = 0
image_add = 1


def animate():
    global image_index
    global image_add

    image_index += image_add  # image_index = image_index + 1
    if image_index >= 3:
        image_add = -1
    if image_index <= 0:
        image_add = 1
    cv.itemconfig(stickman_climb, image=climb_up[image_index])


while True:
    animate()
    root.update()
    time.sleep(0.25)
