import tkinter as tk
import time

root = tk.Tk()
root.title("Run And Jump Animate")
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

run_right = [
    tk.PhotoImage(file="images/run300/run_right_1.png"),
    tk.PhotoImage(file="images/run300/run_right_2.png"),
    tk.PhotoImage(file="images/run300/run_right_3.png"),
    tk.PhotoImage(file="images/run300/run_right_4.png")
]

run_image = cv.create_image(cv_width / 2, cv_height / 2, image=run_left[0])

image_index_l = 0

def run_left_animate():
    global image_index_l
    image_index_l += 1
    cv.itemconfig(run_image, image=run_left[image_index_l % 3])
    root.update()
    time.sleep(0.1)

image_index_r = 0

def run_right_animate():
    global image_index_r
    image_index_r += 1
    cv.itemconfig(run_image, image=run_right[image_index_r % 3])
    root.update()
    time.sleep(0.1)

def stickman_coords():
    stickman_xy = cv.coords(run_image)
    x1 = stickman_xy[0] - 25
    y1 = stickman_xy[1] - 25
    x2 = stickman_xy[0] + 25
    y2 = stickman_xy[1] + 25
    return [x1, y1, x2, y2]

def jump_left_animate():
    cv.itemconfig(run_image, image=run_left[2])
    for i in range(12):
        if 0 <= i < 6:
            cv.move(run_left, -10, -12)
        else:
            cv.move(run_left, -10, 12)
        root.update()
        time.sleep(0.1)
    run_left_animate()

def jump_right_animate():
    cv.itemconfig(run_image, image=run_right[2])
    for i in range(12):
        if 0 <= i < 6:
            cv.move(run_right, 10, -12)
        else:
            cv.move(run_right, 10, 12)
        root.update()
        time.sleep(0.1)
    run_right_animate()

x = 0
y = 0
jump_count = 0

def moving(event):
    global x
    global y
    try:
        while True:
            pos = stickman_coords()
            if event.keysym == "Left":
                if pos[0] <= 0:
                    run_left_animate()
                    cv.move(run_image, 0, 0)
                else:
                    run_left_animate()
                    x = -10
                    y = 0
                    cv.move(run_image, x, y)
            if event.keysym == "Right":
                if pos[2] >= cv_width:
                    run_right_animate()
                    cv.move(run_image, 0, 0)
                else:
                    run_right_animate()
                    x = 10
                    y = 0
                    cv.move(run_image, x, y)
            if event.keysym == "space":
                if y == 0 and x == -10:
                    jump_left_animate()
                    run_left_animate()
                if y == 0 and x == 10:
                    jump_right_animate()
                    run_right_animate()
    except:
        cv.quit()

cv.bind_all('<KeyPress-Left>', moving)
cv.bind_all('<KeyPress-Right>', moving)
cv.bind_all('<space>', moving)

root.mainloop()