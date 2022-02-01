# bitwise operation - logic_not (opposite of input)
import cv2
import numpy as np

img1 = cv2.imread("bit1.png")
cv2.imshow('img1', img1)
#cv2.waitKey(0)


logic_not = cv2.bitwise_not(img1)
cv2.imshow("logic_not", logic_not)
cv2.waitKey(0)

cv2.destroyAllWindows()
