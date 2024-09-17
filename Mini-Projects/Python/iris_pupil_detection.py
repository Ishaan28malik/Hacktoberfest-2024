import cv2
import operator
from tkinter import *
import PIL
import numpy as np
from PIL import ImageTk
from PIL import Image
from tkinter import filedialog
import time

class pupil_detection():
    def __init__(self, image_path):
        self._img = None
        self._img_path = image_path
        self._pupil = None
        self._getCentroid = None
        
    def getImage(self):
        self._img = cv2.imread(self._img_path)
        if type(self._img) == None:
            return False
        else:
            return True
    
    def show_image (self,img):
        cv2.imshow("Pupil Detected",img)
        cv2.waitKey(0)
    
    def getCentroid (self):
        gray_image = cv2.cvtColor(self._img, cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(gray_image,127,255,0)
        M = cv2.moments(thresh)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        self._getCentroid = (cX,cY)
        
    def findPupil (self):
        dst = cv2.fastNlMeansDenoisingColored(self._img,None,10,10,7,21)
        blur = cv2.GaussianBlur(dst,(5,5),0)
        inv = cv2.bitwise_not(blur)
        thresh = cv2.cvtColor(inv, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((2,2),np.uint8)
        erosion = cv2.erode(thresh,kernel,iterations = 1)
        ret,thresh1 = cv2.threshold(erosion,210,255,cv2.THRESH_BINARY)
        cnts, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        flag = 10**4
        final_cnt = None
        for cnt in cnts:
            (x,y),radius = cv2.minEnclosingCircle(cnt)
            distance = abs(self._getCentroid[0]-x)+abs(self._getCentroid[1]-y)
            if distance < flag :
                flag = distance
                final_cnt = cnt
            else:
                continue
        (x,y),radius = cv2.minEnclosingCircle(final_cnt)
        center = (int(x),int(y))
        radius = int(radius)
        f=open("pupil.txt","w")
        f.write(str(radius)+'\n')
        f.close()
        f = open("readings.txt", "a+")
        f.write(str(radius)+'\n')
        f.close()
        
        print("center of pupil at : ",center,"  ","radius : ",radius)
        cv2.circle(self._img,center,radius,(255,0,0),2)
        
        self._pupil = (center[0],center[1],radius)
        self.show_image(self._img)
        f=open("readings.txt","r")
        line=f.readlines()
        #print(line)
        arr=[]
        for i in range(len(line)):
            arr.append(int(line[i][:len(line[i])-1]))
        #print(type(line[0]))
        if len(arr)==6:
            print("The results are as follows:")
            print(" ")
            print("Ratio of 1.1 to 1.2:")
            print("Left = ",arr[0]/arr[2],end="  ")
            print("Right = ",arr[1]/arr[3])
            print(" ")
            print("Ratio of 1.1 to 1.3:")
            print("Left = ",arr[0]/arr[4],end="  ")
            print("Right = ",arr[1]/arr[5])
            print(" ")
            print("Ratio of 1.2 to 1.3:")
            print("Left = ",arr[2]/arr[4],end="  ")
            print("Right = ",arr[3]/arr[5])
            print()
            
        f.close()
    def beginExtraction(self):
        if(self.getImage()):
            self.getCentroid()
            self.findPupil()
        else:
            print('Sorry dude !!! "' + self._img_path + '" is not loadable!!!')

def openFile():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
    label=Label(root,text=root.filename).pack()
    x=root.filename
    f = open("file.txt", "w")
    f.write(x)
    f.close()

def getIris(x):
    img = cv2.imread(x, cv2.IMREAD_COLOR)
    dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    grayed = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    grayedblurred = cv2.blur(grayed, (5, 5))
    detectedIris = cv2.HoughCircles(grayedblurred, 
                                    cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
                            param2 = 30, minRadius = 30, maxRadius = 99) 


    if detectedIris is not None:
            

            detectedIris = np.uint16(np.around(detectedIris))

            for pt in detectedIris[0, :]:
                    a, b, r = pt[0], pt[1], pt[2]
                    print("center of iris at  : ","("+str(a)+", "+str(b)+")"+"    "+"radius : ",r)
                    f=open("pupil.txt","r")
                    line=f.readlines()
                    print("Ratio of radius of pupil to iris for this image is : ",int(line[0][:len(line[0])-1])/b)
                    print()
                    f.close()
                    cv2.circle(img, (a, b), r, (0, 255, 0), 2) 

                    cv2.circle(img, (a, b), 1, (0, 0, 255), 3) 
                    cv2.imshow("Iris Detected", img) 
                    cv2.waitKey(0)
                    break
    

root=Tk()
root.geometry('300x300')
root.title("Pupil and iris extraction")
Label(root,text=" ").pack()
Button(root,text="Select Image",command=openFile).pack()
Label(root,text=" ").pack()
Label(root,text="After selecting. Please close this window to view results!!").pack()
root.mainloop()
with open ("file.txt", "r") as myfile:
    data=myfile.readlines()
x=data[0]
print(x)
print("Running...")
id = pupil_detection(x)
id.beginExtraction()
getIris(x)