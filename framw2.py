import cv2
import matplotlib.pyplot as plt
import numpy as np
cap = cv2.VideoCapture(0)
if cap.isOpened():
    ret , frame= cap.read()
    print(ret)
    print(frame)
else:
    ret = False
img1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.title("Image-Camera")
plt.xticks([])
plt.yticks([])
plt.show()
cap.release()


