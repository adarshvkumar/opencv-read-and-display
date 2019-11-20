#import necessary packages

import cv2

#read the image
#can also add images in other directories by specifying the path

img = cv2.imread("capture.jpg")

#show the image

cv2.imshow("img",img)

cv2.waitKey(0)
