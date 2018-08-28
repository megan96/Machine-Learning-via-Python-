import cv2
import numpy as np
img=cv2.imread("shetty.jpg")
smaller =cv2.pyrDown(img)
larger =cv2.pyrUp(img)
cv2.imshow("Original",img)
cv2.imshow("Small",smaller)
cv2.imshow("Large",larger)

cv2.waitKey(0)
cv2.destroyAllWindows()
