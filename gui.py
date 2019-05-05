import sqlite3
from tkinter import *
import tkinter.font
#################################################################################################################################
db = sqlite3.connect("note.db")
c = db.cursor()

global data

data = " "

global num

global setIndex

global noteTable

def newWin():
    window =Tk.TopLevel(root)

def create_table():
    # notes is the name of the table
    c.execute('CREATE TABLE IF NOT EXISTS noteTable (write TEXT, num REAL)')


def notes():  # Writing

    setIndex = num-1
    c.execute("INSERT INTO noteTable (write,num) values (?,?)",(notes, setIndex))
    num+=1
    db.commit()


def read():  # Reading
    c.execute('SELECT * FROM noteTable')  # FROM notes = selects table "notes"
    data = c.fetchall()
    load.config(text=str(data[num-1]))
    return str(data[num-1])


def save(userIn, num):  # Uploading
    notes = e.get("1.0", END)
    setIndex = num-1
    c.execute("UPDATE noteTable SET write = (?) WHERE num=(?)",
              (userIn, setIndex))
    db.commit()


create_table()
c.close()
db.close()



#################################################################################################################################
global e

def bold():
    current_tags = e.tag_names("sel.first")
    if "bt" in current_tags:
        e.tag_remove("bt", "sel.first", "sel.last")
    else:
        e.tag_add("bt", "sel.first", "sel.last")

root = Tk()

root.title("Sticky Notes")
root.geometry("600x600")


#Side Panel
sidePanel = Frame(root, bg='#CCC', width=500, height=500)
sidePanel.pack(expand=False, fill='both', side='left')

sidebar = Frame(sidePanel, width=150,  height=400, relief='sunken', borderwidth=2)
sidebar.pack(expand=True, side='bottom', anchor='w', fill=BOTH)

#Transparency
root.attributes('-alpha', 0.9)

# main content area
mainarea = Frame(root, bg='#CCC', width=500, height=500)
mainarea.pack(expand=True, fill='both', side='right')

minibar = Frame(sidePanel, width=150, height=200,relief='sunken', borderwidth=3)
minibar.pack(expand=True, side='top', anchor='w', fill=BOTH)

#User Label
user = Label(minibar, text="User: Noel")
user.pack(anchor='n')

#Connection Label
user = Label(minibar, text="Connect to \n Note Database",font=("helvetic",10,'bold'))
user.pack(anchor='n')

#TExt Field
f = Entry(minibar, fg='black')
f.pack()

#Entry TerxtField
e = Text(mainarea, fg='black', width=1000)
e.pack(ipady=50)
e.tag_config("bt", font=("Georgia", "12", "bold"))

#Buttons
save = Button(sidebar, text="Save",font=("Arial", 15, 'bold'))
save.pack(anchor='n',side='top')
new = Button(sidebar, text="New", font=("Arial", 15, 'bold'),command=notes)
new.pack(anchor='n', side='top')
load = Button(sidebar, text="Load", font=("Arial", 15, 'bold'), command=read)
load.pack(anchor='n',side='top')
Bold = Button(mainarea, text="Bold", font=("Arial", 15, 'bold'),command=bold)
Bold.pack(anchor='n', side='top')


root.mainloop()


################################################################################################################
