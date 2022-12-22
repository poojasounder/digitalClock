from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")

label = Label(root, font=("areal", 160, "bold"), bg="black", fg="white")
label.pack(anchor="center", fill="both", expand=1)


def time():
    string = strftime("%H:%M:%S P")
    label.config(text=string)
    label.after(1000, time)


time()
root.mainloop()

