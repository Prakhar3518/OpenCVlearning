import cv2

myimage = cv2.imread('assets/wowpic.jpg',0)

cv2.imshow('imagepage',myimage)  # to open image on a page
cv2.waitKey(0)                      # wait for the time to close the image if 0 will not close till i press a key
cv2.destroyAllWindows()