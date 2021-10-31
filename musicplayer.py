import tkinter as tkr
import pygame
from tkinter.filedialog import Directory, askdirectory
import os
music_player = tkr.Tk()
music_player.title("Music Player")
music_player.geometry("500 X 250")
directory = askdirectory()
os.chdir(directory)
track_list = os.listdir()
play_list = tkr.Listbox(music_player, font ="Helvetica 15 bold", bg="Blue",selectmode= tkr.SINGLE)

for item in track_list:
    pos = 0
    play_list.insert(pos, item)
    pos = pos+1

pygame.init
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop_musicplayer():
    pygame.mixer,music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()


Button_play = tkr.Button(music_player,width=5,height=5, font="Helvetica 10 italic",text="PLAY",command=play,bg="purple",fg="white")
Button_exitplayer = tkr.Button(music_player,width=5,height=5, font="Helvetica 10 italic",text="EXIT PLAYER",command=stop_musicplayer,bg="red",fg="white")
Button_pause = tkr.Button(music_player,width=5,height=5, font="Helvetica 10 italic",text="PAUSE",command=pause,bg="green",fg="white")
Button_unpause = tkr.Button(music_player,width=5,height=5, font="Helvetica 10 italic",text="UNPAUSE",command=unpause,bg="yellow",fg="white")

var= tkr.StringVar()
Song_lable_title = tkr.Label(music_player,font="Helvetica 12 bold", text = var)


Song_lable_title.pack()

Button_play.pack(fill="x")
Button_exitplayer.pack(fill="x")
Button_pause.pack(fill="x")
Button_unpause.pack(fill="x")
play_list.pack(fill="both",expand="yes")


music_player.mainloop()