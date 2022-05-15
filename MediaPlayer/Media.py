import cv2

capture = cv2.VideoCapture("Blue whale swimming.mp4")
print("Opening Video")

while(capture.isOpened()):
    ret,frame = capture.read()
    if ret == True:
        cv2.imshow("Frame", frame)
        if cv2.waitKey(25) & 0xFF==ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
