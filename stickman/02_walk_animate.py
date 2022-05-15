import tkinter as tk
import time

root = tk.Tk()
cv_width = 600
cv_height = 600
cv = tk.Canvas(root, width=cv_width, height=cv_height, bg='black')
cv.pack()

walk_left = [tk.PhotoImage(file="images/walk100/walk_left_1.png"),
             tk.PhotoImage(file="images/walk100/walk_left_2.png"),
             tk.PhotoImage(file="images/walk100/walk_left_3.png")]
stickman_walk_l = cv.create_image(cv_width / 2 + 150, cv_height / 2, image=walk_left[0])

walk_right = [tk.PhotoImage(file="images/walk100/walk_right_1.png"),
              tk.PhotoImage(file="images/walk100/walk_right_2.png"),
              tk.PhotoImage(file="images/walk100/walk_right_3.png")]
stickman_walk_r = cv.create_image(cv_width / 2 - 150, cv_height / 2, image=walk_right[0])

# root.mainloop()

'''创建动画函数'''
left_index = 0


def walk_l():
    global left_index
    left_index += 1
    cv.itemconfig(stickman_walk_l, image=walk_left[left_index % 3])


right_index = 0

def walk_r():
    global right_index
    right_index += 1
    cv.itemconfig(stickman_walk_r, image=walk_right[right_index % 3])  # 0,1,2,0,1,2...


'''创建动画循环'''
try:
    while True:
        walk_l()
        walk_r()
        root.update()
        time.sleep(0.2)
except:
    print(" ")
