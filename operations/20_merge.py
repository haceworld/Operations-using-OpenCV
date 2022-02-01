# Region of Interest (ROI)
import cv2

img = cv2.imread('messi5.jpg')
cv2.imshow('image', img)
cv2.waitKey(0)

print(img.shape)
print(img.size)
print(img.dtype)


b, g, r = cv2.split(img)
img1 = cv2.merge((b,g,r))

cv2.imshow('2nd_image', img1)
cv2.waitKey(0)

cv2.destroyAllWindows()
