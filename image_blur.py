#image blurring
import cv2
import numpy as np
img = cv2.imread("images.jpg")
cv2.imshow("Original Images",img)
cv2.waitKey(0)
blur = cv2.blur(img,(3,3))
cv2.imshow("Blur Image",blur)
cv2.waitKey(0)

gaus = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("gaussian Blur Image",gaus)
cv2.waitKey(0)

median =  cv2.medianBlur(img,5)
cv2.imshow("Median Blur Image",median)
cv2.waitKey(0)

bi =  cv2.bilateralFilter(img,9,75,75)
cv2.imshow("Bi Image",bi)
cv2.waitKey(0)
cv2.destroyAllWindows()
