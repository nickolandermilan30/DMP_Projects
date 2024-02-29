import cv2

img1 = cv2.imread("lena.tif")
bgrgray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
bgrhsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
brightLAB = cv2.cvtColor(img1, cv2.COLOR_BGR2LAB)

cv2.imshow("Image", img1)
 
cv2.imshow("BGR 2 GRAY", bgrgray)
 
cv2.imshow("BGR 2 HSV", bgrhsv)
 
 
cv2.imshow("Bright 2 Lab", brightLAB)
 
 
cv2.waitKey(0)
cv2.destroyAllWindows()
