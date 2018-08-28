import cv2
import numpy as np
img=cv2.imread("images.jpg")
cv2.imshow('Original Image',img)
height,width=img.shape[:2]
print(height)
print(width)
q_h,q_w = height/4,width/4
#around 25%  of image is shifted 
print(q_h)


print(q_w)
#       [1,0,Tx]
#T = [0,1,Ty](img,T,(w,h))
T = np.float32([[1,0,q_w],[0,1,q_h]])
print(T)
img_Trans = cv2.warpAffine(img,T,(width,height))
cv2.imshow("Original Image",img)
cv2.imshow("Transalation",img_Trans)
cv2.waitKey(0)
cv2.destroyAllWindows()
