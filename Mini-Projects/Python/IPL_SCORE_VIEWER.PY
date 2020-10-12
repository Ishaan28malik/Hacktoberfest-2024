from tkinter import *
import requests
from bs4 import BeautifulSoup

# Set our variables
refresh_time = 1000* 2 # Refresh every 2 seconds

# Background colors
original_bg = "#CECCBE"
dark_bg = 'blue'
old_bg = 'sandybrown' # This is no longer used but can be used to replace original_bg
label_old_bg = 'light goldenrod' # This is the old label bg before replacing w/ light/dark theme

# Set up tkinter root window
root = Tk()
root.title("Cricket Score Viewer by SARTHAK")
root.configure(bg=original_bg)

dark_logo= PhotoImage(file="dark_png.png")
normal_logo = PhotoImage(file="ipl.png")
# Darkmode button images
onImg = PhotoImage(file="onbutton.png")
offImg = PhotoImage(file="offbutton.png")

def change_all():

    w1 = Label(root, compound = CENTER,image=dark_logo)
    w1.grid(row=0, columnspan=2 ,pady=5)
    header1.grid(           row=1, columnspan=2,    pady=5)
    team1.grid(             row=2, column=0,        padx=15)
    team2.grid(             row=2, column=1)
    team2_score.grid(       row=3, column=1,        padx=5)
    team1_score.grid(       row=3, column=0,        padx=5)
    result.grid(            row=4, columnspan=2,    pady=5)
    refresh.grid(           row=5, columnspan=2,    pady=5)
    header2.grid(            row=6, columnspan=2,    pady=0)
    darkmodetxt_label.grid( row=8, columnspan=2)
    darkmode_btn.grid(      row=7, columnspan=2,    pady=20)

def rechange_all():

    w1 = Label(root, compound = CENTER,image=normal_logo)
    w1.grid(row=0, columnspan=2 ,pady=5)
    header1.grid(           row=1, columnspan=2,    pady=5)
    team1.grid(             row=2, column=0,        padx=15)
    team2.grid(             row=2, column=1)
    team2_score.grid(       row=3, column=1,        padx=5)
    team1_score.grid(       row=3, column=0,        padx=5)
    result.grid(            row=4, columnspan=2,    pady=5)
    refresh.grid(           row=5, columnspan=2,    pady=5)
    header2.grid(            row=6, columnspan=2,    pady=0)
    darkmodetxt_label.grid( row=8, columnspan=2)
    darkmode_btn.grid(      row=7, columnspan=2,    pady=20)

def darkmode_switch():
    """Function for dark/light theme button"""

    # Check current bg colour
    current_bg = root.cget('bg')
    
    # If current_bg is original, change new_bg to dark (vice versa)
    if current_bg == original_bg:
        new_bg = dark_bg
        darkmodetxt_label.config(text="Dark Mode: ON", bg=new_bg)
        darkmode_btn.config(image=onImg, bg=new_bg, activebackground=new_bg)
        change_all()
      
    elif current_bg == dark_bg:
        new_bg = original_bg
        darkmodetxt_label.config(text="Dark Mode: OFF", bg=new_bg)
        darkmode_btn.config(image=offImg, bg=new_bg, activebackground=new_bg)
        rechange_all()
          
    # Set bg to new_bg, fg to current_bg
    
    root.config(bg=new_bg)
    for item in all_objects:
        item.config(bg=new_bg, fg=current_bg)

        
def get_data():
    """A helper function which fetch the data and update the UI"""
    
    # URL Request
    url ='https://www.cricbuzz.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')

    # Find our data
    team_names = soup.find_all(class_='cb-ovr-flo cb-hmscg-tm-nm')
    team_scores = soup.find_all(class_='cb-ovr-flo')
    result1 = soup.find_all(class_='cb-ovr-flo cb-text-live') # empty if no ongoing game
    result2 = soup.find_all(class_='cb-ovr-flo cb-text-complete')

    # Get name of first 2 teams competing
    dteam1 = team_names[0].get_text()
    dteam2 = team_names[1].get_text()

    # Check if there is an ongoing game & save into variables data we want
    if not result1: # check if result1 is an empty list
        dresult = result2[0].get_text()
        dteam1_score = team_scores[10].get_text()
        dteam2_score = team_scores[12].get_text()

    else:
        dresult = result1[0].get_text()
        dteam1_score = team_scores[8].get_text()
        dteam2_score = team_scores[10].get_text()

    # Update the text labels
    team1.config(text=dteam1)
    team2.config(text=dteam2)
    team1_score.config(text=dteam1_score)
    team2_score.config(text=dteam2_score)
    result.config(text=dresult)
    
    # Loop itself
    root.after(refresh_time, get_data)

# Initialise Tkinter objects
header1 = Label(root, text ='Cricket Live Score by SARTHAK', font ='arial 8')
team1 = Label(root, text='Team 1', font='arial 20', bg=original_bg)
team2 = Label(root, text='Team 2', font='arial 20', bg=original_bg)
team1_score = Label(root, text='hit refresh', font='arial 20', bg=original_bg)
team2_score = Label(root, text='hit refresh', font='arial 20', bg=original_bg)
result = Label(root, text='hit refresh', font='arial 11', bg=original_bg)
refresh = Button(root, text='Refresh', command=get_data, bg=original_bg, fg=dark_bg) # Force refresh
header2 = Label(root, text='Data Collected from Cricbuzz', font='ariel 8')
darkmodetxt_label = Label(root, text="Dark Mode: OFF", font="FixedSys 17", bg=original_bg, fg="green")
darkmode_btn = Button(root, image=offImg, borderwidth=0, command=darkmode_switch, bg=original_bg, activebackground=original_bg, pady=1)
    
# Put our Tkinter objects on grid
w1        = Label(root, compound = CENTER,image=normal_logo)
w1.grid(row=0, columnspan=2 ,pady=5)
header1.grid(           row=1, columnspan=2,    pady=5)
team1.grid(             row=2, column=0,        padx=15)
team2.grid(             row=2, column=1)
team2_score.grid(       row=3, column=1,        padx=5)
team1_score.grid(       row=3, column=0,        padx=5)
result.grid(            row=4, columnspan=2,    pady=5)
refresh.grid(           row=5, columnspan=2,    pady=5)
header2.grid(            row=6, columnspan=2,    pady=0)
darkmodetxt_label.grid( row=8, columnspan=2)
darkmode_btn.grid(      row=7, columnspan=2,    pady=20)

# Set objects for which we want to follow the dark/light theme
all_objects = [team1, team2, team1_score, team2_score, result, refresh]

# Run get_data after mainloop starts
root.after(0, get_data) # This triggers get_data which has a root.after ==> hence loops itself

# Run the app
try:
    print("CTRL + C to close or click close button")
    root.mainloop()
except KeyboardInterrupt:
    print("Thanks for using Cricket Score Viewer")
except Exception as e:
    print("UnKnownError:%s. Please report to the author"%str(e))