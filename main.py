from tkinter import *

window = Tk()
window.minsize(width=500, height=300)

label = Label(text="It is a label")
label["text"] = "It is a label"
label.grid(column=0, row=0)


def button_clicked():
    label["text"] = entry.get()


button = Button()

button.config(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
button2 = Button()

button2.config(text="Click Me", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
entry = Entry(width=10)
entry.grid(column=3, row=2)

window.mainloop()
