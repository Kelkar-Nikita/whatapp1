import tkinter
from tkinter import *
from tkinter.ttk import *
def clicked():
    pgbar.start(10)

def stopped():
    pgbar.stop()

root = tkinter.Tk()
root.geometry("500x500")

# pgbar =Progressbar(
#     root,
#     length = 200,
#     orient=HORIZONTAL,
#     mode ="determinate",
#     maximum =100,
#     value =10,
# )
# pgbar.pack()
pgbar =Progressbar(
    root,
    length =200,
    orient=HORIZONTAL,
    mode ="indeterminate",
    # maximum =100,
    # value =10,
)
pgbar.pack()
btn =Button(
    root,
    text ="click Me",
    command =clicked,
)
btn.pack()
btn2= Button(
    root,
    text="stop",
    command =stopped,
)
btn2.pack()
root.mainloop()