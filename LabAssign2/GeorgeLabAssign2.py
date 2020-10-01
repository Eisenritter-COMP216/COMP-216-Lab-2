"""
Filename: GeorgeLabAssign2.py
Created By: George Zhou
Date: September 28, 2020
Description: A simple Python GUI App
Last Modified: September 28, 2020
"""
import string
from tkinter import Tk, W, E, N, S, StringVar, ttk, IntVar, messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("George's Python GUI App")
root.geometry = ('1024x768')

mainframe = ttk.Frame(root, width=600, height=450, padding='5 5 5 5')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Import and create Image
size = (64, 64)  # Define Size of Thumbnail
logoImg = Image.open("Python Logo.png")  # Opens the png Iimage file
logoImg = logoImg.resize(size)  # Resize the logo Image
logo = ImageTk.PhotoImage(logoImg)  # set logo to image

# row 0
ttk.Label(mainframe, image=logo).grid(column=1, row=0, sticky=(E, W))

# Working with String Input
fullName = StringVar

# row 1
ttk.Label(mainframe, text='Full Name').grid(column=0, row=1, sticky=W)
fullNameEntry = ttk.Entry(mainframe, width=30, textvariable=fullName)
fullNameEntry.grid(column=1, row=1, sticky=W)

# row 2
ttk.Label(mainframe, text='Residency').grid(column=0, row=2, sticky=W)

style = ttk.Style()
style.configure("inner.TFrame")

# row 2 radio box
radioframe = ttk.Frame(mainframe, padding='5 5 5 5', style="inner.TFrame", relief="sunken", borderwidth=5)
radioframe.grid(column=1, row=2, sticky=(N, W, E, S))
rv = StringVar()
rdButDom = ttk.Radiobutton(radioframe, text="Domestic", variable=rv, value="dom")
rdButDom.grid(row=0, sticky=W)
rdButIntl = ttk.Radiobutton(radioframe, text="International", variable=rv, value="intl")
rdButIntl.grid(row=1, sticky=W)

# row 3 Program Combo Box
ttk.Label(mainframe, text='Program').grid(row=3, column=0, sticky=W)
ProgramComboBox = ttk.Combobox(mainframe, values=["Gaming", "Health", "Software"])
ProgramComboBox.grid(row=3, column=1, sticky=(W, E))

# row 4 CheckBox
ttk.Label(mainframe, text='Courses').grid(column=0, row=4, sticky=W)
chkboxFrame = ttk.Frame(mainframe, padding='5 5 5 5', style="inner.TFrame", relief="sunken", borderwidth=5)
chkboxFrame.grid(column=1, row=4, columnspan=2, sticky=(N, W, E, S))

# Check Box Buttons
varCourseList = []
SelectedList = []
varCourse = StringVar()
varCourse2 = StringVar()
varCourse3 = StringVar()
ChkC1 = ttk.Checkbutton(chkboxFrame, text="Programming 1", variable=varCourse)
ChkC1.grid(row=0, sticky=W)
ChkC2 = ttk.Checkbutton(chkboxFrame, text="Web Page Design", variable=varCourse2)
ChkC2.grid(row=1, sticky=W)
ChkC3 = ttk.Checkbutton(chkboxFrame, text="Software Engineering Fundamentals", variable=varCourse3)
ChkC3.grid(row=2, sticky=W)
varCourseList.append(ChkC1)
varCourseList.append(ChkC2)
varCourseList.append(ChkC3)


# Row 5
# Course List Helper Function
def addtolist():
    if varCourse.get() == '1':
        SelectedList.append("comp100")
    if varCourse2.get() == '1':
        SelectedList.append("comp213")
    if varCourse3.get() == '1':
        SelectedList.append("comp120")
    return ' '.join(SelectedList)


# Button Functions
def reset():
    SelectedList.clear()
    fullNameEntry.delete(0,'end')
    rv=''
    varCourse.set(0)
    varCourse2.set(0)
    varCourse3.set(0)
    ProgramComboBox.set('')

def OK():
    messagebox.showinfo('Form Information',
                        f'Username:{fullNameEntry.get()} \n Residency: {rv.get()} \n Courses: {addtolist()}\n'
                        f'Program: {ProgramComboBox.get()}')
    reset()


def Exit():
    root.destroy()


ttk.Button(mainframe, text="Reset", command=reset).grid(row=5, column=0, sticky=(W, E))
ttk.Button(mainframe, text="Ok", command=OK).grid(row=5, column=1, sticky=(W, E))
ttk.Button(mainframe, text="Exit", command=Exit).grid(row=5, column=2, sticky=(W, E))

# start program
root.mainloop()
