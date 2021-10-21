import tkinter
from PIL import ImageTk,Image
import pygame

window= tkinter.Tk ()
window.title("HERO ISL")
window.geometry("2000x2000")

bgimage=Image.open(r"img\sl.png")
resize01=bgimage.resize((1366,768),Image.ANTIALIAS)
bgimage=ImageTk.PhotoImage(resize01)

tkinter.Label(window,image=bgimage).place(relwidth=1,relheight=1)

label=tkinter.Label(window,text="Welcome to the Hero ISL Page",font=('arial',25,'italic')).pack()

#initialize mixer


#frame1=tkinter.Frame(window)

pygame.mixer.init()
def pl(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def play():
    song=r"audio\eb.mp3"
    pl(song)
def play2():
    song=r"audio\atk.mp3"
    pl(song)
def play3():
    song=r"audio\bfc.mp3"        
    pl(song)
def play4():
    song=r"audio\cfc.mp3"           
    pl(song)
def play5():
    song=r"audio\fcgoa.mp3"
    pl(song)
def play6():
    song=r"audio\hfcc.mp3"
    pl(song)
def play7():
    song=r"audio\jfc.mp3"           
    pl(song)
def play8():
    song=r"audio\kfc.mp3"
    pl(song)
def play9():
    song=r"audio\mgoa.mp3"
    pl(song)
def play10():
    song=r"audio\ogoa.mp3"
    pl(song)
def play11():
    song=r"audio\nfc.mp3"
    pl(song)

def stop():
    pygame.mixer.music.stop()

#images 

#first=tkinter.PhotoImage(file=r"C:\Users\hp\Desktop\logo1.png")
first=Image.open(r"img\eb.png")
resize1=first.resize((150,150),Image.ANTIALIAS)
first=ImageTk.PhotoImage(resize1)

second=Image.open(r"img\mb.png")
resize2=second.resize((150,150),Image.ANTIALIAS)
second=ImageTk.PhotoImage(resize2)

third=Image.open(r"img\bengaluru.png")
resize3=third.resize((150,150),Image.ANTIALIAS)
third=ImageTk.PhotoImage(resize3)

fourth=Image.open(r"img\chennai.png")
resize4=fourth.resize((150,150),Image.ANTIALIAS)
fourth=ImageTk.PhotoImage(resize4)

fifth=Image.open(r"img\fcgoa.png")
resize5=fifth.resize((150,150),Image.ANTIALIAS)
fifth=ImageTk.PhotoImage(resize5)

sixth=Image.open(r"img\hfc.png")
resize6=sixth.resize((150,150),Image.ANTIALIAS)
sixth=ImageTk.PhotoImage(resize6)

seventh=Image.open(r"img\jfc.png")
resize7=seventh.resize((150,150),Image.ANTIALIAS)
seventh=ImageTk.PhotoImage(resize7)

eighth=Image.open(r"img\kfc.png")
resize8=eighth.resize((150,150),Image.ANTIALIAS)           
eighth=ImageTk.PhotoImage(resize8)

ninth=Image.open(r"img\mfc.png")
resize9=ninth.resize((150,150),Image.ANTIALIAS)      
ninth=ImageTk.PhotoImage(resize9)

tenth=Image.open(r"img\ofc.png")            
resize10=tenth.resize((150,150),Image.ANTIALIAS)
tenth=ImageTk.PhotoImage(resize10)

eleventh=Image.open(r"img\nfc.png")
resize11=eleventh.resize((150,150),Image.ANTIALIAS)       
eleventh=ImageTk.PhotoImage(resize11)


#Buttons for Row1


first_button=tkinter.Button(window, image=first,borderwidth=0,height=150,width=150,command=play)
second_button=tkinter.Button(window, image=second,borderwidth=0,height=150,width=150,command=play2)
third_button=tkinter.Button(window, image=third,borderwidth=0,height=150,width=150,command=play3)
fourth_button=tkinter.Button(window, image=fourth,borderwidth=0,height=150,width=150,command=play4)

fifth_button=tkinter.Button(window, image=fifth,borderwidth=0,height=150,width=150,command=play5)
sixth_button=tkinter.Button(window, image=sixth,borderwidth=0,height=150,width=150,command=play6)
seventh_button=tkinter.Button(window, image=seventh,borderwidth=0,height=150,width=150,command=play7)
eighth_button=tkinter.Button(window, image=eighth,borderwidth=0,height=150,width=150,command=play8)

ninth_button=tkinter.Button(window, image=ninth,borderwidth=0,height=150,width=150,command=play9)
tenth_button=tkinter.Button(window, image=tenth,borderwidth=0,height=150,width=150,command=play10)
eleventh_button=tkinter.Button(window , image=eleventh,borderwidth=0,height=150,width=150,command=play11)

stop_1=tkinter.Button(window,text="Stop Song",command=stop)



#placing buttons
first_button.place(x=150,y=100)
second_button.place(x=450,y=100)
third_button.place(x=750,y=100)
fourth_button.place(x=1050,y=100)

fifth_button.place(x=150,y=300)
sixth_button.place(x=450,y=300)
seventh_button.place(x=750,y=300)
eighth_button.place(x=1050,y=300)

ninth_button.place(x=300,y=500)
tenth_button.place(x=600,y=500)
eleventh_button.place(x=900,y=500)

stop_1.place(x=1050,y=650)

window.mainloop()
