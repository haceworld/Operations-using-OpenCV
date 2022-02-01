# add 2 images - must be same size

import cv2

img1 = cv2.imread('messi5.jpg')
img1 = cv2.resize(img1, (512, 512))

img2 = cv2.imread('est.jpg')
img2 = cv2.resize(img2, (512, 512))

img = cv2.add(img1, img2)

cv2.imshow('image', img)
cv2.waitKey(0)


# make an image more dominant that the other
# cv2.addWeighted(img1, img1_weight, img2, img1_weight, scaler_digit)
img_weighted = cv2.addWeighted(img1, .6, img2, .4, 0)
cv2.imshow('image_weighted', img_weighted)
cv2.waitKey(0)


cv2.destroyAllWindows()
