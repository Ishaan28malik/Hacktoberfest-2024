import cv2
from gtts import gTTS
from playsound import playsound

def play_audio(path_of_audio):
    playsound(path_of_audio)

def convert_to_audio(text):
    my_audio=gTTS(text)
    my_audio.save("audio.mp3")
    play_audio("audio.mp3")

convert_to_audio("Starting Face detection ")


face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
capture=cv2.VideoCapture(0)

while True:
    _, img = capture.read()
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4)

    #Creates a tracking Rectangle around the Face
    #(255,0,0)- changing these values will give Different Colors

    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 6)

    # It flips the image to get the Frames Correctly ,
    # 0 - Flip the Frames Vertically and 1 - Flips the Frames Horizontally
    Flip = cv2.flip(img, 1)

    # You can Change the Parameters to Resize the Window or
    resized = cv2.resize(Flip, (int(800), (int(600))))

    # Display the frame
    cv2.imshow('Capturing',resized)
    key=cv2.waitKey(1)& 0xFF

    # if the `Space` key was pressed, break from the loop
    if key==ord(' '):
        break

capture.release()

# do a bit of cleanup
cv2.destroyAllWindows()
