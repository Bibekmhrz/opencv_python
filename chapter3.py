#Resizing and cropping

#Resizing an image

import cv2
import numpy as np
img = cv2.imread("Resources/photo.jpg")
print(img.shape)  #to know the size of image

imgResize = cv2.resize(img, (300,200))
print(imgResize.shape)

imgCropped = img[0:200, 200:500] #cropping an image

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)

