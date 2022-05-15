import cv2
import numpy as np

capture=cv2.VideoCapture("Review.mp4")
print("Error Opening Video")

while(capture.isOpened()):
    ret,frame=capture.read()
    if ret==True:
        cv2.imshow("Frame",frame)
        if cv2.waitKey(25) & 0xFF==ord("q"):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()