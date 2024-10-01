pip3 install opencv-python qrcode numpy
Generate QR Code
First, let's start by generating QR codes, it is basically straightforward using qrcode library:
import qrcode
# example data
data = "https://www.thepythoncode.com"
# output file name
filename = "site.png"
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)
This will generate a new image file in the current directory with the name of "site.png", which contains a QR code image of the data specified (in this case, this website URL), will look something like this:
You can also use this library to have full control with QR code generation using the qrcode.QRCode() class, in which you can instantiate and specify the size, fill color, back color, and error correction, like so:
import qrcode
import numpy as np
# data to encode
data = "https://www.thepythoncode.com"
# instantiate QRCode object
qr = qrcode.QRCode(version=1, box_size=10, border=4)
# add data to the QR code
qr.add_data(data)
# compile the data into a QR code array
qr.make()
# print the image shape
print("The shape of the QR image:", np.array(qr.get_matrix()).shape)
# transfer the array into an actual image
img = qr.make_image(fill_color="white", back_color="black")
# save it to a file
img.save("site_inversed.png")
So in the creation of QRCode class, we specify the version parameter, which is an integer from 1 to 40 that controls the size of the QR code image (1 is small, 21x21 matrix, 40 is 185x185 matrix), but this will be overwritten when the data doesn't fit the size you specify. In our case, it will scale up to version 3 automatically.
box_size parameter controls how many pixels each box of the QR code is, whereas the border controls how many boxes thick the border should be.

We then add the data using the qr.add_data() method, compiles it to an array using qr.make() method, and then make the actual image using qr.make_image() method. We specified white as the fill_color and black as the back_color, which is the exact opposite of the default QR code, check it out:
  import cv2
# initalize the cam
cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    # check if there is a QRCode in the image
    if bbox is not None:
        # display the image with lines
        for i in range(len(bbox)):
            # draw all lines
            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
        if data:
            print("[+] QR Code detected, data:", data)
    # display the result
    cv2.imshow("img", img)    
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
