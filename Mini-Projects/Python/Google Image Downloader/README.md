# About the project
In this project i made a google image downloader in python which is a class GoogleImage and give the method getImg a name or text whose image you 
want to download from google and it will download it with the help of web automation tool called selenium 

---
just add the file in your project and import the class and use like bellow

```python

image_downloader = GoogleImage()
image_downloader.getImg(name='hacktoberfest', count=1)
image_downloader.close()
```

---
above code will make a folder gdownload in CWD and will save the 'hacktoberfest' image in that folder 
