import cv2
import numpy as np
img=cv2.imread("shetty.jpg")

height,width=img.shape[:2]
rot_mat = cv2.getRotationMatrix2D((width/2,height/2),70,0.7)
img_Trans = cv2.warpAffine(img,rot_mat,(width,height))

cv2.imshow("Rotated  Image",img_Trans)
cv2.imshow("Original Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
