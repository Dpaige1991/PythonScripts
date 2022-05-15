import tkinter as tk
import time

root = tk.Tk()
cv_width = 1280
cv_height = 720
cv = tk.Canvas(root, width=cv_width, height=cv_height, bg='black')
cv.pack()

jump_right = [
    tk.PhotoImage(file="images/jump/jump_right_1.png"),
    tk.PhotoImage(file="images/jump/jump_right_2.png"),
    tk.PhotoImage(file="images/jump/jump_right_3.png"),
    tk.PhotoImage(file="images/jump/jump_right_4.png"),
    tk.PhotoImage(file="images/jump/jump_right_5.png"),
    tk.PhotoImage(file="images/jump/jump_right_6.png"),
    tk.PhotoImage(file="images/jump/jump_right_7.png"),
    tk.PhotoImage(file="images/jump/jump_right_8.png"),
    tk.PhotoImage(file="images/jump/jump_right_9.png")
]
jump_left = [
    tk.PhotoImage(file="images/jump/jump_left_1.png"),
    tk.PhotoImage(file="images/jump/jump_left_2.png"),
    tk.PhotoImage(file="images/jump/jump_left_3.png"),
    tk.PhotoImage(file="images/jump/jump_left_4.png"),
    tk.PhotoImage(file="images/jump/jump_left_5.png"),
    tk.PhotoImage(file="images/jump/jump_left_6.png"),
    tk.PhotoImage(file="images/jump/jump_left_7.png"),
    tk.PhotoImage(file="images/jump/jump_left_8.png"),
    tk.PhotoImage(file="images/jump/jump_left_9.png")
]
stickman_jump = cv.create_image(cv_width / 2, cv_height / 2, image=jump_right[0])

right_image_index = 0
left_image_index = 0


def jump_right_animate():
    global right_image_index
    right_image_index += 1
    current_right_image = right_image_index % 9
    # if right_image_index > 8:
    if current_right_image == 0:
        cv.move(stickman_jump, 80, 0)
    cv.itemconfig(stickman_jump, image=jump_right[current_right_image])
    root.update()
    time.sleep(0.15)


def jump_left_animate():
    global left_image_index
    left_image_index += 1
    current_left_image = left_image_index % 9
    # if left_image_index > 8:
    if current_left_image == 0:
        cv.move(stickman_jump, -80, 0)
    cv.itemconfig(stickman_jump, image=jump_left[current_left_image])
    root.update()
    time.sleep(0.15)


def stickman_coords():
    stickman_xy = cv.coords(stickman_jump)  # [x, y]
    x1 = stickman_xy[0] - 50
    y1 = stickman_xy[1] - 50
    x2 = stickman_xy[0] + 50
    y2 = stickman_xy[1] + 50
    return [x1, y1, x2, y2]


def jump_right_move(event):
    pos = stickman_coords()
    if event.keysym == "Right":
        cv.move(stickman_jump, 8, 0)
    jump_right_animate()

def jump_left_move(event):
    pos = stickman_coords()
    if event.keysym == "Left":
        cv.move(stickman_jump, -8, 0)
    jump_left_animate()


cv.bind_all('<KeyPress-Left>', jump_left_move)
cv.bind_all('<KeyPress-Right>', jump_right_move)

root.mainloop()
