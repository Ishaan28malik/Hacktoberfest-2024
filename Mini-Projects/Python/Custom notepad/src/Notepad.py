"""
Notepad.py is a custom notepad I made with various features that were lacking in the original version of windows notepad.

For more details, you can check out my project repository at :
https://github.com/SVijayB/Custom-notepad
"""
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
from datetime import datetime
from tkinter.colorchooser import askcolor
import webbrowser
from textwrap import *

Shortcut_dark = True
Shortcut_journal = True

class Shortcuts:
    def New_file(self):
        try:
            if not text.compare("end-1c", "==", "1.0"):
                if askyesno("Notepad", "Do you want to save changes?"):
                    writing()
                else:
                    text.delete(1.0, END)
        except:
            pass

    def Save_as(self):
        try:
            if not text.compare("end-1c", "==", "1.0"):
                writing()
            else:
                if askyesno("Notepad", "Do you want to save an empty file?"):
                    writing()
        except:
            pass

    def Google(self):
        try:
            search_term = text.selection_get()
            url = "https://www.google.com/search?q={}".format(search_term)
            webbrowser.open(url)
        except:
            webbrowser.open("https://www.google.com")

    def Date(self):
        now = datetime.now()
        data = (str(now.strftime("%d/%m/%Y")) + "\n")
        text.insert(INSERT, data)
    
    def Time(self):
        now = datetime.now()
        data = (str(now.strftime("%H:%M:%S")) + "\n")
        text.insert(INSERT, data)

    def Date_and_time(self):
        now = datetime.now()
        data = (str(now.strftime("%d/%m/%Y %H:%M:%S")) + "\n")
        text.insert(INSERT, data)
    
    def Text_colour(self):
        (triple,color) = askcolor()
        if(color):
            text.config(fg = color)
    
    def No_Format(self):
        try:
            text.tag_remove("bold", "sel.first", "sel.last")
            text.tag_remove("italic", "sel.first", "sel.last")
            text.tag_remove("underline", "sel.first", "sel.last")
            text.tag_remove("highlight", "sel.first", "sel.last")
            text.config(font = ("Agency FB", 20))
        except:
            pass

    def Bold(self):
        try:
            current_tags = text.tag_names("sel.first")
            if("bold" in current_tags):
                text.tag_remove("bold", "sel.first", "sel.last")
            else:
                text.tag_remove("italic", "sel.first", "sel.last")
                text.tag_remove("underline", "sel.first", "sel.last")
                text.tag_add("bold", "sel.first", "sel.last")
                text.tag_config("bold",font = ("Agency FB", 20, "bold"))
        except:
            pass

    def Italic(self):
        try:
            current_tags = text.tag_names("sel.first")
            if("italic" in current_tags):
                text.tag_remove("italic", "sel.first", "sel.last")
            else:
                text.tag_remove("bold", "sel.first", "sel.last")
                text.tag_remove("underline", "sel.first", "sel.last")
                text.tag_add("italic", "sel.first", "sel.last")
                text.tag_config("italic",font = ("Agency FB", 20, "italic"))
        except:
            pass

    def Underline(self):
        try:
            current_tags = text.tag_names("sel.first")
            if("underline" in current_tags):
                text.tag_remove("underline", "sel.first", "sel.last")
            else:
                text.tag_remove("bold", "sel.first", "sel.last")
                text.tag_remove("italic", "sel.first", "sel.last")
                text.tag_add("underline", "sel.first", "sel.last")
                text.tag_config("underline",font = ("Agency FB", 20, "underline"))
        except:
            pass

    def Highlight(self):
        try:
            current_tags = text.tag_names("sel.first")
            if("highlight" in current_tags):
                text.tag_remove("highlight", "sel.first", "sel.last")
            else:
                text.tag_add("highlight", "sel.first", "sel.last")
                text.tag_config("highlight", background = "yellow", foreground = "black")
        except:
            pass

    def Background(self):
        (triple,color) = askcolor()
        if(color):
            text.config(bg = color)

    def View_help(self):
        webbrowser.open("https://github.com/SVijayB/Custom-notepad/tree/master#Usage")

    def Dark_mode(self):
        global Shortcut_dark
        if(Shortcut_dark):
            text.config(bg = "black", fg = "white", insertbackground = "white")
            Shortcut_dark = False
            dark.set(1)
        else:
            text.config(bg = "white", fg = "black", insertbackground = "black")
            Shortcut_dark = True
            dark.set(0)
    
    def Journal_mode(self):
        global Shortcut_journal
        if(Shortcut_journal):
            Date_and_time()
            Shortcut_journal = False
            journal.set(1)
        else:
            Shortcut_journal = True
            journal.set(0)

if __name__=="__main__":

    def writing():
        filename = filedialog.asksaveasfilename()
        if filename:
            content = text.get(1.0, END)
            open(filename, 'w').write(content)

    # Commands : 

    def New_file():
        try:
            if not text.compare("end-1c", "==", "1.0"):
                if askyesno("Notepad", "Do you want to save changes?"):
                    writing()
                else:
                    text.delete(1.0, END)
        except:
            pass

    def Open_file():
        try:
            if not text.compare("end-1c", "==", "1.0"):
                if askyesno("Notepad", "Do you want to save changes?"):
                    writing()
                    text.delete(1.0, END)
            file = open(filedialog.askopenfilename(), "r")
            text.delete(1.0, END)
            if(file!=""):
                content = file.read()
                text.insert(INSERT, content)
        except:
            pass

    def Save_as():
        try:
            if not text.compare("end-1c", "==", "1.0"):
                writing()
            else:
                if askyesno("Notepad", "Do you want to save an empty file?"):
                    writing()
        except:
            pass
    
    def Close():
        try:
            if not text.compare("end-1c", "==", "1.0"):
                choice = askyesnocancel("Notepad", "Do you want to save changes?")
                if choice:
                    writing()
                    root.destroy()
                elif choice is None:
                    pass
                else:
                    root.destroy()
            else:
                root.destroy()
        except:
            pass

    # Edit Menu :

    def Cut():
        try:
            text.clipboard_clear()
            text.clipboard_append(text.selection_get())
            text.delete(SEL_FIRST, SEL_LAST)
        except:
            pass
    
    def Copy():
        try:
            text.clipboard_clear()
            text.clipboard_append(text.selection_get())
        except:
            pass

    def Paste():
        try:
            data = text.selection_get(selection = "CLIPBOARD")
            text.insert(INSERT, data)
        except:
            pass

    def Delete():
        try:
            text.delete(SEL_FIRST, SEL_LAST)
        except:
            pass

    def Select_all():
        text.tag_add('sel', '1.0', 'end')
        return "break"

    def Clear_screen():
        text.delete(1.0, END)

    def Google():
        try:
            search_term = text.selection_get()
            url = "https://www.google.com/search?q={}".format(search_term)
            webbrowser.open(url)
        except:
            webbrowser.open("https://www.google.com")

    # Insert Menu : 

    def Date():
        now = datetime.now()
        data = (str(now.strftime("%d/%m/%Y")) + "\n")
        text.insert(INSERT, data)
    
    def Time():
        now = datetime.now()
        data = (str(now.strftime("%H:%M:%S")) + "\n")
        text.insert(INSERT, data)

    def Date_and_time():
        now = datetime.now()
        data = (str(now.strftime("%d/%m/%Y %H:%M:%S")) + "\n")
        text.insert(INSERT, data)

    # Format Menu : 

    def Text_colour():
        (triple,color) = askcolor()
        if(color):
            text.config(fg = color)
    
    def No_Format():
        try:
            text.tag_remove("bold", "sel.first", "sel.last")
            text.tag_remove("italic", "sel.first", "sel.last")
            text.tag_remove("underline", "sel.first", "sel.last")
            text.tag_remove("highlight", "sel.first", "sel.last")
            text.config(font = ("Agency FB", 20))
        except:
            pass

    def Bold():
        try:
            current_tags = text.tag_names("sel.first")
            if("bold" in current_tags):
                text.tag_remove("bold", "sel.first", "sel.last")
            else:
                text.tag_remove("italic", "sel.first", "sel.last")
                text.tag_remove("underline", "sel.first", "sel.last")
                text.tag_add("bold", "sel.first", "sel.last")
                text.tag_config("bold",font = ("Agency FB", 20, "bold"))
        except:
            pass

    def Italic():
        try:
            current_tags = text.tag_names("sel.first")
            if("italic" in current_tags):
                text.tag_remove("italic", "sel.first", "sel.last")
            else:
                text.tag_remove("bold", "sel.first", "sel.last")
                text.tag_remove("italic", "sel.first", "sel.last")
                text.tag_add("italic", "sel.first", "sel.last")
                text.tag_config("italic",font = ("Agency FB", 20, "italic"))
        except:
            pass

    def Underline():
        try:
            current_tags = text.tag_names("sel.first")
            if("underline" in current_tags):
                text.tag_remove("underline", "sel.first", "sel.last")
            else:
                text.tag_remove("bold", "sel.first", "sel.last")
                text.tag_remove("italic", "sel.first", "sel.last")
                text.tag_add("underline", "sel.first", "sel.last")
                text.tag_config("underline",font = ("Agency FB", 20, "underline"))
        except:
            pass

    def Highlight():
        try:
            current_tags = text.tag_names("sel.first")
            if("highlight" in current_tags):
                text.tag_remove("highlight", "sel.first", "sel.last")
            else:
                text.tag_add("highlight", "sel.first", "sel.last")
                text.tag_config("highlight", background = "yellow", foreground = "black")
        except:
            pass

    # Personalize Menu : 

    def Background():
        (triple,color) = askcolor()
        if(color):
            text.config(bg = color)

    def Dark_mode():
        if(dark.get()==1):
            text.config(bg = "black", fg = "white", insertbackground = "white")
        else:
            text.config(bg = "white", fg = "black", insertbackground = "black")
    
    def Journal_mode():
        if(journal.get()==1):
            Date_and_time()
        else:
            pass

    # Help Menu : 

    def View_help():
        webbrowser.open("https://github.com/SVijayB/Custom-notepad/tree/master#Usage")
    
    def Feedback():
        webbrowser.open("https://github.com/SVijayB/Custom-notepad/issues/new/choose")

    # On_launch and Exit : 

    def On_launch():
        preferences = open("../temp/preferences.txt","r").read()
        preferences = preferences.splitlines()
        if(preferences[0]=="Dark = 1"):
            dark.set(1)
            Dark_mode()
        content = open("../temp/temp.txt","r").read()
        text.insert(CURRENT, content)
        msg = text.get(1.0, END)   
        text.delete("end-1l","end")
        if(preferences[1]=="Journal = 1"):
            journal.set(1)
            Journal_mode()

    def Exit():
        preferences = "Dark = %d\nJournal = %d" %(dark.get(),journal.get())
        open("../temp/preferences.txt", 'w').write(preferences)
        content = text.get(1.0, END)
        open("../temp/temp.txt", 'w').write(content)
        root.destroy()

    root = Tk()
    root.iconbitmap("../assets/images/Icon.ico")
    root.title("Notepad")
    main_menu = Menu(root)
    root.config(menu = main_menu)

    commands = Menu(root, tearoff=False)
    main_menu.add_cascade(label = "File" , menu = commands)
    commands.add_command(label = "New File", command = New_file, accelerator='Ctrl+N')
    root.bind("<Control-n>", Shortcuts.New_file)
    commands.add_command(label = "Open...", command = Open_file)
    commands.add_command(label = "Save As...", command = Save_as, accelerator='Ctrl+S')
    root.bind("<Control-s>", Shortcuts.Save_as)
    commands.add_command(label = "Exit", command = Close, accelerator='Alt+F4')

    edit_menu = Menu(root, tearoff=False)
    main_menu.add_cascade(label = "Edit" , menu = edit_menu)
    edit_menu.add_command(label = "Cut", command = Cut, accelerator='Ctrl+X')
    edit_menu.add_command(label = "Copy", command = Copy, accelerator='Ctrl+C')
    edit_menu.add_command(label = "Paste", command = Paste, accelerator='Ctrl+V')
    edit_menu.add_separator()
    edit_menu.add_command(label = "Delete", command = Delete)
    edit_menu.add_command(label = "Select All", command = Select_all, accelerator='Ctrl+A')
    edit_menu.add_command(label = "Clear Screen", command = Clear_screen)
    edit_menu.add_separator()
    edit_menu.add_command(label = "Search with Google...", command = Google, accelerator='Ctrl+E')
    root.bind("<Control-e>", Shortcuts.Google)

    insert_menu = Menu(root, tearoff=False)
    main_menu.add_cascade(label = "Insert", menu = insert_menu)
    insert_menu.add_command(label = "Current Date", command = Date, accelerator='Ctrl+D')
    root.bind("<Control-d>", Shortcuts.Date)
    insert_menu.add_command(label = "Current Time", command = Time, accelerator='Ctrl+T')
    root.bind("<Control-t>", Shortcuts.Time)
    insert_menu.add_command(label = "Date And Time", command = Date_and_time, accelerator='Ctrl+Shift+D')
    root.bind("<Control-Shift-d>", Shortcuts.Date_and_time)

    format_menu = Menu(root, tearoff=False)
    main_menu.add_cascade(label = "Format", menu = format_menu)
    format_menu.add_command(label = "Font", command = Text_colour, accelerator='Ctrl+F')
    root.bind("<Control-f>", Shortcuts.Text_colour)
    format_menu.add_separator()
    format_menu.add_command(label = "Bold", command = Bold, accelerator='Ctrl+B')
    root.bind("<Control-b>", Shortcuts.Bold)
    format_menu.add_command(label = "Italic", command = Italic, accelerator='Ctrl+Y')
    root.bind("<Control-y>", Shortcuts.Italic)
    format_menu.add_command(label = "Underline", command = Underline, accelerator='Ctrl+U')
    root.bind("<Control-u>", Shortcuts.Underline)
    format_menu.add_command(label = "Highlight Text", command = Highlight, accelerator='Ctrl+W')
    root.bind("<Control-w>", Shortcuts.Highlight)
    format_menu.add_command(label = "Remove Format", command = No_Format, accelerator='Ctrl+Q')
    root.bind("<Control-q>", Shortcuts.No_Format)

    personalize_menu = Menu(root, tearoff=False)
    main_menu.add_cascade(label = "Personalize", menu = personalize_menu)
    personalize_menu.add_command(label = "Background", command = Background, accelerator='Alt+X')
    root.bind("<Alt-x>", Shortcuts.Background)
    personalize_menu.add_command(label = "Text Colour", command = Text_colour, accelerator='Ctrl+F')
    personalize_menu.add_separator()
    dark = IntVar()
    personalize_menu.add_checkbutton(label = "Dark Mode", variable = dark, command = Dark_mode, accelerator='Alt+D')
    root.bind("<Alt-d>", Shortcuts.Dark_mode)
    journal = IntVar()
    personalize_menu.add_checkbutton(label = "Journal mode", variable = journal, command = Journal_mode, accelerator='Alt+J')
    root.bind("<Alt-j>", Shortcuts.Journal_mode)

    help_menu = Menu(root, tearoff=False)
    main_menu.add_cascade(label = "Help", menu = help_menu)
    help_menu.add_command(label = "View Help", command = View_help, accelerator='Alt+H')
    root.bind("<Alt-h>", Shortcuts.View_help)
    help_menu.add_command(label = "Send Feedback", command = Feedback)

    text = Text(root, height = 17, width = 70,wrap = WORD, font = ("Agency FB", 20))
    text.focus()
    scrollbar = Scrollbar(root, command = text.yview)
    scrollbar.config(command = text.yview)
    text.config(yscrollcommand = scrollbar.set)
    scrollbar.pack(side = RIGHT, fill=Y)
    text.pack()
    root.resizable(0,0)
    On_launch()
    root.protocol("WM_DELETE_WINDOW",Exit)

    root.mainloop()