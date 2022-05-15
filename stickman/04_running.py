import tkinter as tk
import time

'''Step1:设置窗口(设置游戏画布)'''

window = tk.Tk()

canvas_width = 1280
canvas_height = 720

canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

run_left = [
    tk.PhotoImage(file="images/run/run_left_1.png"),
    tk.PhotoImage(file="images/run/run_left_2.png"),
    tk.PhotoImage(file="images/run/run_left_4.png")
]
run_right = [
    tk.PhotoImage(file="images/run/run_right_1.png"),
    tk.PhotoImage(file="images/run/run_right_2.png"),
    tk.PhotoImage(file="images/run/run_right_4.png")
]
run_image = canvas.create_image(canvas_width / 2, canvas_height / 2, image=run_left[0])

run_left_index = 0
run_right_index = 0


def run_left_animate():
    global run_left_index
    canvas.itemconfig(run_image, image=run_left[run_left_index % 3])  # 0, 1, 2, 0, 1...
    run_left_index += 1
    window.update()
    time.sleep(0.1)


def run_right_animate():
    global run_right_index
    canvas.itemconfig(run_image, image=run_right[run_right_index % 3])
    run_right_index += 1
    window.update()
    time.sleep(0.1)


def stickman_coords():
    stickman_xy = canvas.coords(run_image)
    x1 = stickman_xy[0] - 50
    y1 = stickman_xy[1] - 50
    x2 = stickman_xy[0] + 50
    y2 = stickman_xy[1] + 50
    return [x1, y1, x2, y2]


def running(event):
    try:
        while True:
            pos = stickman_coords()
            if event.keysym == "Left":
                if pos[0] <= 0:
                    run_left_animate()
                    canvas.move(run_image, 0, 0)
                else:
                    run_left_animate()
                    canvas.move(run_image, -20, 0)
            if event.keysym == "Right":
                if pos[2] >= canvas_width:
                    run_right_animate()
                    canvas.move(run_image, 0, 0)
                else:
                    run_right_animate()
                    canvas.move(run_image, 20, 0)
    except:
        window.quit()


canvas.bind_all('<KeyPress-Left>', running)
canvas.bind_all('<KeyPress-Right>', running)

window.mainloop()
