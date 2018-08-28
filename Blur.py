#blurring
import cv2
import numpy as np
img = cv2.imread("images.jpg")
cv2.imshow("Original Images",img)
cv2.waitKey(0)
k = np.ones((3,3),np.float32)/9
blurred = cv2.filter2D(img,-1,k)
cv2.imshow("3x3 kernel blurring",blurred)
cv2.waitKey(0)
k7 = np.ones((9,9),np.float32)/49
blurred2 = cv2.filter2D(img,-1,k7)
cv2.imshow("9x9 kernel blurring",blurred2)
cv2.waitKey(0)
cv2.destroyAllWindows()
