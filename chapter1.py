import cv2
print("Package Imported")
#For reading images
img = cv2.imread( "Resources/photo.jpg")     #imread() is a function to read images

cv2.imshow("Output", img)      # 'imshow() is a function to show the output of images'
cv2.waitKey(1000)   #for delay in milli second i.e 1000 is 1second

#For Reading Video
cap =cv2.VideoCapture("Resources/video.mp4")    #for reading video

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#For webcam
cap = cv2.VideoCapture(0) #zero for default webca. if have multiple cam then can set value according to capid
cap.set(3, 640)   #width of id no 3 as 640
cap.set(4,480)    #height of id 4 as 480
cap.set(10,1000)   #increasing a brightness

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
