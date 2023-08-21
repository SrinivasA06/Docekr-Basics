import cv2
import numpy as np
url = "rtmp://65.49.44.136/live"
cap = cv2.VideoCapture(url)
while(True):
    camera, frame = cap.read()
    print('success')
    #cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q==ord("q"): 
        break
#cv2.destroyAllWindows()
