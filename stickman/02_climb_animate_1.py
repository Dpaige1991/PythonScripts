import tkinter as tk
import time

root = tk.Tk()
cv_width = 1280
cv_height = 720
cv = tk.Canvas(root, width=cv_width, height=cv_height, bg='black')
cv.pack()

climb_up = [
    tk.PhotoImage(file="images/climb/climb_up1.png"),
    tk.PhotoImage(file="images/climb/climb_up2.png"),
    tk.PhotoImage(file="images/climb/climb_up3.png"),
    tk.PhotoImage(file="images/climb/climb_up4.png"),
    tk.PhotoImage(file="images/climb/climb_up5.png"),
    tk.PhotoImage(file="images/climb/climb_up6.png")
]
stickman_climb = cv.create_image(cv_width / 2, cv_height / 2, image=climb_up[0])

image_index = 0


def animate():
    global image_index
    image_index += 1
    cv.itemconfig(stickman_climb, image=climb_up[image_index % 6])


while True:
    animate()
    root.update_idletasks()
    root.update()
    time.sleep(0.2)
