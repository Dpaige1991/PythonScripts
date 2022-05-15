import tkinter as tk
import time

root = tk.Tk()
root.title("Walk Animate")
cv_width = 1280
cv_height = 720
cv = tk.Canvas(root, width=cv_width, height=cv_height, bg='black')
cv.pack()

run_left = [
    tk.PhotoImage(file="images/run300/run_left_1.png"),
    tk.PhotoImage(file="images/run300/run_left_2.png"),
    tk.PhotoImage(file="images/run300/run_left_3.png"),
    tk.PhotoImage(file="images/run300/run_left_4.png")
]
stickman_run_l = cv.create_image(cv_width / 2 + 300, cv_height / 2, image=run_left[0])

run_right = [
    tk.PhotoImage(file="images/run300/run_right_1.png"),
    tk.PhotoImage(file="images/run300/run_right_2.png"),
    # tk.PhotoImage(file="images/run300/run_right_3.png"),
    tk.PhotoImage(file="images/run300/run_right_4.png")
]
stickman_run_r = cv.create_image(cv_width / 2 - 300, cv_height / 2, image=run_right[0])

image_index_l = 0


def left_animate():
    global image_index_l
    image_index_l += 1
    cv.itemconfig(stickman_run_l, image=run_left[image_index_l % 4])


image_index_r = 0


def right_animate():
    global image_index_r
    image_index_r += 1
    cv.itemconfig(stickman_run_r, image=run_right[image_index_r % 3])


try:
    while True:
        left_animate()
        right_animate()
        root.update()
        time.sleep(0.12)
except:
    print("Exit")
