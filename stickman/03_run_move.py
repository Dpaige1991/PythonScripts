import tkinter as tk
import time

root = tk.Tk()
cv_width = 1280
cv_height = 720
cv = tk.Canvas(root, width=cv_width, height=cv_height, bg='black')
cv.pack()

run_left = [
    tk.PhotoImage(file="images/run100/run_left_1.png"),
    tk.PhotoImage(file="images/run100/run_left_2.png"),
    # tk.PhotoImage(file="images/run/run_left_3.png"),
    tk.PhotoImage(file="images/run100/run_left_4.png")
]
run_right = [
    tk.PhotoImage(file="images/run100/run_right_1.png"),
    tk.PhotoImage(file="images/run100/run_right_2.png"),
    # tk.PhotoImage(file="images/run/run_right_3.png"),
    tk.PhotoImage(file="images/run100/run_right_4.png")
]
run_image = cv.create_image(cv_width / 2, cv_height / 2, image=run_right[0])

run_left_index = 0
run_right_index = 0


def run_left_animate():
    global run_left_index
    cv.itemconfig(run_image, image=run_left[run_left_index % 3])
    run_left_index += 1
    root.update()
    time.sleep(0.15)


def run_right_animate():
    global run_right_index
    cv.itemconfig(run_image, image=run_right[run_right_index % 3])
    run_right_index += 1
    root.update()
    time.sleep(0.15)


def stickman_coords():
    stickman_xy = cv.coords(run_image)
    x1 = stickman_xy[0] - 50
    y1 = stickman_xy[1] - 50
    x2 = stickman_xy[0] + 50
    y2 = stickman_xy[1] + 50
    return [x1, y1, x2, y2]


def run_left_move(event):
    pos = stickman_coords()
    if event.keysym == "Left":
        if pos[0] <= 0-20:
            cv.move(run_image, 0, 0)
        else:
            cv.move(run_image, -20, 0)
    run_left_animate()


def run_right_move(event):
    pos = stickman_coords()
    if event.keysym == "Right":
        if pos[2] >= cv_width + 20:
            cv.move(run_image, 0, 0)
        else:
            cv.move(run_image, 20, 0)
    run_right_animate()


cv.bind_all('<KeyPress-Left>', run_left_move)
cv.bind_all('<KeyPress-Right>', run_right_move)

root.mainloop()
