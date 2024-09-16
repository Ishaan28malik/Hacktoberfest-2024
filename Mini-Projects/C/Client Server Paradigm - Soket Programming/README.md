<!-- ABOUT THE PROJECT -->
## About the Project

This project was build to learn the fundamentals of socket programming. Berkeley socket interface is used for implementing whatever I learned.
The main features of this program are :
1. Implemented client server paradigm.
2. Functionality of sending and receiving text messages, basically a chat application.
3. Functionality of sending various files such as text/images/audio/video.

### Screenshots
Running the server and client on same machine
![Product Name Screen Shot][screenshot1]

Sending a file
![Product Name Screen Shot][screenshot2]

Sending an txt file
![Product Name Screen Shot][screenshot4]

Sending a image
![Product Name Screen Shot][screenshot5]

Sending a audio file
![Product Name Screen Shot][screenshot6]

Sending a video file
![Product Name Screen Shot][screenshot7]

Chatting with the server
![Product Name Screen Shot][screenshot8]




### Installation

1. Open the terminal run the server and give a port no.
```sh
./server portno
```
2. Open another terminal and run the client. If you are running the code in same machine then give address as 127.0.0.1 or if you are running the client in another machine then pass the server ip adderess (Can be found usisng ifconfig). Make sure that the port no. in both the cases are same
```sh
./client 127.0.0.1 portno
```

<!-- MARKDOWN LINKS & IMAGES -->
[screenshot1]: screenshots/ss1.png
[screenshot2]: screenshots/ss2.png
[screenshot3]: screenshots/ss3.png
[screenshot4]: screenshots/ss4.png
[screenshot5]: screenshots/ss5.png
[screenshot6]: screenshots/ss6.png
[screenshot7]: screenshots/ss7.png
[screenshot8]: screenshots/ss8.png
