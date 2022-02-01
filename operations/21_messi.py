# copy messi ball

import cv2

img = cv2.imread('messi5.jpg')
cv2.imshow('image', img)
cv2.waitKey(0)

print(img.dtype)

ball = img[280:340, 330:390]

img[273:333, 100:160] = ball
cv2.imshow('2nd_image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
