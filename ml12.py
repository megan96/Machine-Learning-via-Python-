import cv2
img = cv2.imread("flower.jpg")
cv2.imshow("Hello  Flower",img)
cv2.waitKey(0)
 
#0 is any interrupt and any other value will be ascii value for interrupt 
cv2.destroyAllWindows()
