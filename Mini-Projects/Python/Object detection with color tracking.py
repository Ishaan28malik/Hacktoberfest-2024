# HSV (Hue,Saturation and Value) value...
# This is used to seperate color illuminance from color information
# This is generally used at times when color description is important

# Hue is the color
# saturation is the amount of color
# value is brightness of color

import cv2
import numpy as np

def pass_fn(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Track the color")
cv2.createTrackbar("lower_hue","Track the color",0,255,pass_fn)
cv2.createTrackbar("lower_sat","Track the color",0,255,pass_fn)
cv2.createTrackbar("lower_value","Track the color",0,255,pass_fn)
cv2.createTrackbar("upper_hue","Track the color",255,255,pass_fn)
cv2.createTrackbar("upper_sat","Track the color",255,255,pass_fn)
cv2.createTrackbar("upper_value","Track the color",255,255,pass_fn)

while True:
    #frame = cv2.imread('smarties.png')
    ret,frame = cap.read()
    if ret == False:
        continue
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_hue = cv2.getTrackbarPos('lower_hue',"Track the color")
    l_sat = cv2.getTrackbarPos('lower_sat', "Track the color")
    l_value = cv2.getTrackbarPos('lower_value', "Track the color")

    u_hue = cv2.getTrackbarPos('upper_hue', "Track the color")
    u_sat = cv2.getTrackbarPos('upper_sat', "Track the color")
    u_value = cv2.getTrackbarPos('upper_value', "Track the color")

    lower_blue = np.array([l_hue,l_sat,l_value])
    upper_blue = np.array([u_hue,u_sat,u_value])

    # for blue color: l_b=[110,50,50]
    # for blue color: u_b=[130,255,255]

    # mask to find only the specific color
    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)&0xff
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()