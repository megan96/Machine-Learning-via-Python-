#Sketch Function
import cv2
import numpy as np
def sketch(image):
    img = cv2.cvtColor(image,cv2.cvtColor_BGR2GRAY)
    img_b = cv2.GaussianBlur(img,(5,5),0)
    can_edge = cv2.Canny(img_b,10,70)
    ret,mask = cv2.threshold(can_edge,70,255,cv2.THRESH_BINARY_INV)
    return mask
cap = cv2.VideoCapture(0)
while True:
    ret ,frame= cap.read()
    cv2.imshow("Live Sketch",sketch(frame))
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()
