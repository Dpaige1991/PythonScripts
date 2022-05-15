import tkinter as tk
import time

root = tk.Tk()
cv_w = 600
cv_h = 600
cv = tk.Canvas(root, width=cv_w, height=cv_h, bg='black')
cv.pack()

jump_right = [
    tk.PhotoImage(file="images/jump300/jump_right_1.png"),
    tk.PhotoImage(file="images/jump300/jump_right_2.png"),
    tk.PhotoImage(file="images/jump300/jump_right_3.png"),
    tk.PhotoImage(file="images/jump300/jump_right_4.png"),
    tk.PhotoImage(file="images/jump300/jump_right_5.png"),
    tk.PhotoImage(file="images/jump300/jump_right_6.png"),
    tk.PhotoImage(file="images/jump300/jump_right_7.png"),
    tk.PhotoImage(file="images/jump300/jump_right_8.png"),
    tk.PhotoImage(file="images/jump300/jump_right_9.png")
]
stickman_jump = cv.create_image(cv_w / 2, cv_h / 2, image=jump_right[0])

image_index = 0


def jump_animate():
    global image_index
    image_index += 1
    cv.itemconfig(stickman_jump, image=jump_right[image_index % 9])


while True:
    jump_animate()
    root.update_idletasks()
    root.update()
    time.sleep(0.15)
