import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

# val=0
def clicked():
    # global val
    if var.get() < 5:
        # val = val+1
        var.set(1+var.get())
        lbl.config(text="Pressed "+str(var.get())+" out of 5 times")
    else:
        messagebox.showwarning("warning","You already pressed 5 times")

root = tkinter.Tk()
root.geometry("500x500")

var =IntVar()
# var variable created and set value
var.set(0)
# progress bar
pgbar =Progressbar(
    root,
    orient =HORIZONTAL,
    mode ='determinate',
    maximum =5,
    length = 200,
    variable = var,
)
pgbar.pack(pady=40)
btn =tkinter.Button(
    root,
    text ="Click mi 5 time",
    command = clicked,
)
btn.pack(pady=20)

lbl =Label(
    root,
    font =("consolas",16),

)
lbl.pack()

root.mainloop()