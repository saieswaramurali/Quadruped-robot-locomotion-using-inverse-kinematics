import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (cap.isOpened()) : 
    while True :
        ret,image=cap.read()
        cv2.imshow("ik",image)
        if cv2.waitkey(30) & 0xff == ord('q') :
            break
        
    cap.release()
    cv2.destroyAllWindows()

else :
    print("Alet ! camera disconnected")