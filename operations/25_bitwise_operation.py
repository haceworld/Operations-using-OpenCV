# bitwise operation on images - mask(binary images)
import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

print(img1.shape)
cv2.imshow("img1", img1)
cv2.waitKey(0)


#img2 = cv2.imread("image1.png")
#img2 = cv2.resize(img2, (500, 250))



img2 = np.zeros((250, 500, 3), np.uint8)
img2 = cv2.rectangle(img2, (250, 0), (500, 250), (255, 255, 255), -1)


cv2.imwrite('bit1.png', img1)
cv2.imwrite('bit2.png', img2)



print(img2.shape)
cv2.imshow("img2", img2)
cv2.waitKey(0)

cv2.destroyAllWindows()
