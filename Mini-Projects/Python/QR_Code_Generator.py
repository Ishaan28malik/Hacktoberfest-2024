#Creating a QR Code Generator using Python


import pyqrcode
url='https://techychefs.blogspot.com/'     #In url you can provide any valid URL
web=pyqrcode.create(url)
web.svg('techychefs.svg',scale=10)         #scale defines the size of QR Code
