import cv2
import numpy as np
from PIL import ImageGrab
import threading
from tkinter import *

window = Tk()
window.geometry("500x200+460+170")
window.resizable(0, 0)
window.configure(bg='#030818')

screen_size = (1920, 1080)
recording = threading.Event()

def recorder():
    print("recording started")

window.mainloop()