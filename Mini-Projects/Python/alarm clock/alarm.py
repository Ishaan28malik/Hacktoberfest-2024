from time import sleep

import pygame
import datetime

pygame.init()
pygame.mixer.init()

h = int(input("Enter hour:-"))
m = int(input("Enter min :-"))

while 1:
    if h == datetime.datetime.now().hour and m == datetime.datetime.now().minute:
        pygame.mixer.music.load("alarm.mp3")
        pygame.mixer.music.play()
        sleep(1)
        break


