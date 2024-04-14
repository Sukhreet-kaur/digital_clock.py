
from tkinter import *
from tkinter.ttk import *
from time import strftime #helps to analyse current time
root=Tk()
root.title("Digital Clock")
def time():
    string=strftime("%I:%M:%S %p")
    label.config(text=string) #giving the tkinter label test as the current time
    label.after(1000,time) #calling the strftime fucntion to know current time every second
label=Label(root,font=('Arial',80),background='red',foreground='white')
label.pack(anchor="center")
time()
mainloop()