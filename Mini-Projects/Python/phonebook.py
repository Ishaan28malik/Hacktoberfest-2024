from tkinter import *



def which_selected():
    print("At {0}".format(select.curselection()))
    return int(select.curselection()[0])


def add_entry():
    phonelist.append([fnamevar.get(), lnamevar.get(), phonevar.get()])
    set_select()


def update_entry():
    phonelist[which_selected()] = [fnamevar.get(),
                                   lnamevar.get(),
                                   phonevar.get()]


def delete_entry():
    del phonelist[which_selected()]
    set_select()


def load_entry():
    fname, lname, phone = phonelist[which_selected()]
    fnamevar.set(fname)
    lnamevar.set(lname)
    phonevar.set(phone)


def make_window():
    global fnamevar, lnamevar, phonevar, select
    win = Tk()
    win.title("Phonebook")
    win.configure(background='purple')
    

    frame1 = Frame(win)      #this frame contans all the entry labels
    frame1.pack()

    Label(frame1, text="First Name").grid(row=0, column=0, sticky=W)
    fnamevar = StringVar()
    fname = Entry(frame1, textvariable=fnamevar)
    fname.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Last Name").grid(row=1, column=0, sticky=W)
    lnamevar = StringVar()
    lname = Entry(frame1, textvariable=lnamevar)
    lname.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Phone").grid(row=2, column=0, sticky=W)
    phonevar = StringVar()
    phone = Entry(frame1, textvariable=phonevar)
    phone.grid(row=2, column=1, sticky=W)

    frame2 = Frame(win)       
    frame2.pack()
    b1 = Button(frame2, text=" Add  ", command=add_entry)
    b2 = Button(frame2, text="Update", command=update_entry)
    b3 = Button(frame2, text="Delete", command=delete_entry)
    b4 = Button(frame2, text="Load  ", command=load_entry)
    b5 = Button(frame2, text="Refresh", command=set_select)
    b1.pack(side=LEFT,padx=10)
    b2.pack(side=LEFT,padx=10)
    b3.pack(side=LEFT,padx=10)
    b4.pack(side=LEFT,padx=10)
    b5.pack(side=LEFT,padx=10)


    b1.configure(background='green')
    b2.configure(background='cyan')
    b3.configure(background='red')
    b4.configure(background='yellow')
    b5.configure(background='orange')

    
    frame3 = Frame(win)       
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=10)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT, fill=BOTH, expand=1)
    return win


def set_select():
    phonelist.sort(key=lambda record: record[1])
    select.delete(0, END)
    for fname, lname, phone in phonelist:
        select.insert(END, "{0}, {1}".format(lname, fname))


phonelist=[]


win = make_window()

set_select()
win.mainloop()
