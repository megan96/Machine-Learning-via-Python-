#Edge detection
import cv2
import numpy as np
img = cv2.imread("images.jpg",0)
h,w = img.shape
#dx and dy operator for x and y axis.
s_x = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
s_y = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

cv2.imshow("Original Images",img)
cv2.waitKey(0)


cv2.imshow("Sobel x image",s_x)
cv2.waitKey(0)


cv2.imshow("Sobel y image",s_y)
cv2.waitKey(0)

s_or  = cv2.bitwise_or(s_x,s_y)
cv2.imshow("Sobel or image",s_or)



cv2.waitKey(0)

laplacian =  cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("Laplacian image",laplacian)
cv2.waitKey(0)

can =  cv2.Canny(img,20,170)
cv2.imshow("Canny Edge",can)
cv2.waitKey(0)
cv2.destroyAllWindows()
