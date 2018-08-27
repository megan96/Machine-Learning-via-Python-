import cv2
img= cv2.imread("flower.jpg")
img_HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
b = img_HSV.copy()
b[:,:,0] = 0
b[:,:,1] = 0
g = img_HSV.copy()
g[:,:,0] = 0
g[:,:,2] = 0
r = img_HSV.copy()
r[:,:,1] = 0
r[:,:,2] = 0

cv2.imshow("blue",r)
cv2.imshow("red",b)
cv2.imshow("green",g)

cv2.waitKey(0)
cv2.destroyAllWindows()
