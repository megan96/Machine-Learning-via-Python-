import cv2
import numpy as np
img=cv2.imread("images.jpg")
img_Trans = cv2.transpose(img)

cv2.imshow("Rotated  Image",img_Trans)
cv2.imshow("Original Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
