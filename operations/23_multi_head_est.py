# copy messi ball

import cv2

img = cv2.imread('est.jpg')
cv2.imshow('image', img)
cv2.waitKey(0)

print(img.dtype)

head = img[70:240, 330:500]

img[300:470, 560:730] = head   # imh[height_high: height_low, width: width_far]
img[300:470, 90:260] = head



cv2.imshow('2nd_image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()


# head = img[70:240, 330:500]
# img[300:470, 560:730] = head
