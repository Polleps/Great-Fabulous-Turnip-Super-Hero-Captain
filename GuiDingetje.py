__author__ = 'Polle'
from tkinter import *

root = Tk()
root.size("200x200")
frame1 = Frame(root)
frame2 = Frame(root)

frame1.pack(side=TOP)


button1 = Button(frame1, text="Test", fg="red")
button1.grid(row=0, sticky=W)


root.mainloop()