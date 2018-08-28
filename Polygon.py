import cv2
import numpy as np
img = np.zeros((512,512,3),np.uint8)
pts = np.array([[40,0],[0,0],[20,34.641]],np.int32)

#pts1 = np.array([[10,32],[20,5],[40,32]],np.int32)
cv2.imshow("Original Image",img)
cv2.polylines(img,[pts],True ,(200,200,0),1)
#cv2.polylines(img,[pts1],True ,(200,200,0),1)
cv2.imshow("Polygon",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
