import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    ret , frame= cap.read()
    cv2.imshow("Live Sketch",frame)
    #13 is ascii value for enter and 24 for esc
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()

