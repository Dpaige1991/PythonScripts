import tkinter as tk
import time

root = tk.Tk()
cv_width = 1280
cv_height = 720
cv = tk.Canvas(root, width=cv_width, height=cv_height, bg='black')
cv.pack()

walk_left = [
    tk.PhotoImage(file="images/walk100/walk_left_1.png"),
    tk.PhotoImage(file="images/walk100/walk_left_2.png"),
    tk.PhotoImage(file="images/walk100/walk_left_3.png")]

walk_right = [
    tk.PhotoImage(file="images/walk100/walk_right_1.png"),
    tk.PhotoImage(file="images/walk100/walk_right_2.png"),
    tk.PhotoImage(file="images/walk100/walk_right_3.png")]

stickman_walk = cv.create_image(cv_width / 2, cv_height / 2, image=walk_right[0])

walk_left_index = 0
walk_right_index = 0


def walk_left_animate():
    global walk_left_index
    walk_left_index += 1
    cv.itemconfig(stickman_walk, image=walk_left[walk_left_index % 3])
    root.update()
    time.sleep(0.2)


def walk_right_animate():
    global walk_right_index
    walk_right_index += 1
    cv.itemconfig(stickman_walk, image=walk_right[walk_right_index % 3])  # -1, -2, 0, -1, -2, 0
    root.update()
    time.sleep(0.2)


def stickman_coords():
    stickman_xy = cv.coords(stickman_walk)  # [x, y]
    x1 = stickman_xy[0] - 50
    y1 = stickman_xy[1] - 50
    x2 = stickman_xy[0] + 50
    y2 = stickman_xy[1] + 50
    return [x1, y1, x2, y2]


def walk_move(event):
    pos = stickman_coords()  # [x1, y1, x2, y2]
    if event.keysym == "Left":
        if pos[0] <= 0-30:
            cv.move(stickman_walk, 0, 0)
        else:
            cv.move(stickman_walk, -9, 0)
    walk_left_animate()

    if event.keysym == "Right":
        if pos[2] >= cv_width+30:
            cv.move(stickman_walk, 0, 0)
        else:
            cv.move(stickman_walk, 9, 0)
    walk_right_animate()


cv.bind_all('<KeyPress-Left>', walk_move)
cv.bind_all('<KeyPress-Right>', walk_move)

root.mainloop()
