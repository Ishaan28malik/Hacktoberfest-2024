import vlc
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

root = tk.Tk()
root.title("Video Player")
root.geometry("800x600")

video_frame = ttk.Frame(root)
video_frame.place(x=5, y=5, width=790, height=490)

media_player = vlc.MediaPlayer()

play_button = ttk.Button(root, text="Play", command=lambda: media_player.play())
play_button.place(x=5, y=500, width=100)

pause_button = ttk.Button(root, text="Pause", command=lambda: media_player.pause())
pause_button.place(x=110, y=500, width=100)

stop_button = ttk.Button(root, text="Stop", command=lambda: media_player.stop())
stop_button.place(x=215, y=500, width=100)

open_button = ttk.Button(root, text="Open", command=lambda: open_file())
open_button.place(x=320, y=500, width=100)

def open_file():
       filename = filedialog.askopenfilename()
       media = vlc.Media(filename)
       media_player.set_media(media)

root.mainloop()
