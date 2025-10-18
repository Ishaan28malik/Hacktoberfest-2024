import cv2
#make sure you have numpy and opencv
#pip install numpy opencv-python
cam = cv2.VideoCapture(0)
facedata=cv2.CascadeClassifier('face.xml')
# for those who don't have camera

while 3 > 2:
    x,y=cam.read()
    print(y)
    facecord = facedata.detectMultiScale(y)
    print(facecord)
    for (x1,y1,w,h) in facecord:
        cv2.rectangle(y,(x1,y1),(x1+w,y1+h),(0,255,0),3)
        faceonly=y[y1:y1+h,x1:x1+w]
    cv2.imshow('live',y)
    cv2.imshow('face',faceonly)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break