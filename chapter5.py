#Warp Prespective

import cv2
import numpy as np

img = cv2.imread("Resources/photo.jpg")

print(img.shape)
width, height = 400,200
pts1 = np.float32([[29,82],[383,26],[52,261],[413,174]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)