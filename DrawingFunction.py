import cv2
img = cv2.imread("Dog.jpg")
img = cv2.rectangle(img,(384,0),(500,128),(0,0,255),10)
cv2.imshow("Show Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Result_2.png',img)