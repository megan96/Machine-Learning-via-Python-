import cv2
import numpy as np
img=cv2.imread("shetty.jpg")

height,width=img.shape[:2]


s_row, s_col = int(height*.00), int(width*.00)
e_row, e_col = int(height*.50), int(width*.50)


s1_row, s1_col = int(height*.00), int(width*.50)
e1_row, e1_col = int(height*.50), int(width*1.0)


s3_row, s3_col = int(height*.50), int(width*.00)
e3_row, e3_col = int(height*1.0), int(width*.50)


s4_row, s4_col = int(height*.50), int(width*.50)
e4_row, e4_col = int(height*1.0), int(width*1.0)


crop = img[s_row:e_row,s_col:e_col]
crop1 = img[s1_row:e1_row,s1_col:e1_col]
crop2 = img[s3_row:e3_row,s3_col:e3_col]
crop3 = img[s4_row:e4_row,s4_col:e4_col]
cv2.imshow("Original Image",img)
cv2.waitKey(0)
cv2.imshow("Cropped",crop)
cv2.waitKey(0)
cv2.imshow("Cropped1",crop1)
cv2.waitKey(0)
cv2.imshow("Cropped2",crop2)
cv2.waitKey(0)
cv2.imshow("Cropped3",crop3)
cv2.waitKey(0)
cv2.destroyAllWindows()
