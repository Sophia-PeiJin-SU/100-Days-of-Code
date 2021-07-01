from tkinter import *


def button_clicked():
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=input_text.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
# my_label["text"] = "New Text"
# my_label.config(text="New Text")

# button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# entry
input_text = Entry(width=10)
# input_text.pack()
input_text.grid(column=3, row=2)

window.mainloop()


# unlimited position argument
# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
#
# print(add(3, 4, 5, 6, 7))


# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)
