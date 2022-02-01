# bitwise operation - logic_or (when atleast one is 1)
import cv2
import numpy as np

img1 = cv2.imread("bit1.png")
cv2.imshow('img1', img1)
#cv2.waitKey(0)

img2 = cv2.imread("bit2.png")
cv2.imshow("img2", img2)
#cv2.waitKey(0)

logic_or = cv2.bitwise_or(img1, img2,)
cv2.imshow("logic_or", logic_or)
cv2.waitKey(0)

cv2.destroyAllWindows()
