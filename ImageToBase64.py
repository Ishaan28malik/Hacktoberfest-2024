import base64 
import sys

string = "" # initialised blank string

path='' # Add your image files path with file name 

with open(path, "rb") as imageFile:
    string = base64.b64encode(imageFile.read())
    print(string)
    print(len(string))
    print(sys.getsizeof(string))