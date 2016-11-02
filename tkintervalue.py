from Tkinter import *
import tkMessageBox

def hello1Back():
    hasil = int(E2.get()) + int(E1.get())
    tkMessageBox.showinfo("Hello Python", str(hasil))

def hello2Back():
    hasil = int(E2.get()) - int(E1.get())
    tkMessageBox.showinfo("Hello Python", str(hasil))

def hello3Back():
    hasil = int(E2.get()) * int(E1.get())
    tkMessageBox.showinfo("Hello Python", str(hasil))

def hello4Back():
    hasil = float(E2.get()) / float(E1.get())
    tkMessageBox.showinfo("Hello Python", str(hasil))

