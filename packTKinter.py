import Tkinter
from Tkinter import *

root = Tk()
frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root)
frame2.pack(side=BOTTOM)

w = Label(frame1, text="Red", bg="red", fg="white")
w.pack(side=LEFT)
w = Label(frame1, text="Green", bg="green", fg="black")
w.pack(side=LEFT)
w = Label(frame1, text="Blue", bg="blue", fg="white")
w.pack(side=LEFT)
w = Button(frame2, text="Hello")
w.pack()

mainloop()

