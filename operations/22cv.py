# copy messi ball
import cv2

img = cv2.imread('est.jpg')
#img = cv2.imread('messi5.jpg')

cv2.imshow('image', img)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ", " + str(y)
        cv2.putText(img, strXY, (x,y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)


cv2.setMouseCallback('image', click_event)


cv2.waitKey(0)
cv2.destroyAllWindows()
