import _portaudio as pa
import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something")
    audio = recognizer.listen(source)

print("you said")
print(recognizer.recognize_google(audio))
