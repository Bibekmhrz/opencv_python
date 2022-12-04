#shapes and texts

import cv2
import numpy as np

# img = np.zeros((512, 512))  #blank image is created
img = np.zeros((512, 512, 3), np.uint8)
print(img)
#img[:] = 250,0,0  #value for blue color
#img[200:300] = 250,0,0

cv2.line(img,(0,0),(img.shape[1], img.shape[0]),(0,255,0), 3)  #for st. line star, end point, color   that 3 is for thickness
cv2.rectangle(img, (0,0), (250,250),(0,0,255), 2)   #cv2.FILLED in the place of 3 will fill the color in rectangle box
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img,"OPENCV", (300, 100), cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
cv2.imshow("Image", img)

cv2.waitKey(0)