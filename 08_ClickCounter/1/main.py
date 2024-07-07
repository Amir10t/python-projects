from tkinter import *

counter = 0
def print_hello():
    global counter
    counter += 1
    count_lbl.config(text="Clicked : {}".format(counter))

window = Tk()

window.title("Click Counter")

count_lbl = Label(window,text="Clicked : 0", font=("Tahoma, 20"))
count_lbl.pack()
Button(window,text="Click ME!",command=print_hello).pack()

window.geometry("300x300")

window.mainloop()