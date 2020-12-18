from tkinter import *

window = Tk()
window.minsize(width=500, height=300)

# entry

entry = Entry()
entry.grid(column=1, row=0)

# label
mile_label = Label()
mile_label.config(text="Miles")
mile_label.grid(column=1, row=1)

# label
equal_label = Label()
equal_label["text"] = "is equal to"
equal_label["padx"] = 20

equal_label.grid(column=0, row=2)

# label

ans_label = Label(text="0")
ans_label.grid(column=1, row=2)

# label
km_label = Label(text="Km")
km_label.grid(column=2, row=2)


def calculate():
    user_input = entry.get()
    km = int(int(user_input)*1.6)
    ans_label["text"] = f"{km}"

# button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)

window.mainloop()
