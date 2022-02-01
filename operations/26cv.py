# bitwise operation - logic_and (when both are 1:1)
import cv2
import numpy as np

img1 = cv2.imread("bit1.png")
cv2.imshow('img1', img1)
#cv2.waitKey(0)

img2 = cv2.imread("bit2.png")
cv2.imshow("img2", img2)
#cv2.waitKey(0)

logic_and = cv2.bitwise_and(img1, img2,)
cv2.imshow("logic_and", logic_and)
cv2.waitKey(0)

cv2.destroyAllWindows()
