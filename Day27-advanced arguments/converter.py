from tkinter import *


def button_clicked():
    result = round(float(input_text.get()) * 1.60943, 2)
    calculate_label.config(text=f"{result}")


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=50, pady=50)

input_text = Entry(width=7, font=("Arial", 16))
input_text.grid(column=1, row=0)


miles_label = Label(text="Miles", font=("Arial", 16))
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=10)

equal_to_label = Label(text="is  equal to", font=("Arial", 16))
equal_to_label.grid(column=0, row=1)
equal_to_label.config(padx=20, pady=10)

calculate_label = Label(text="0", font=("Arial", 16))
calculate_label.grid(column=1, row=1)
calculate_label.config(padx=20, pady=10)

km_label = Label(text="Km", font=("Arial", 16))
km_label.grid(column=2, row=1)
km_label.config(padx=20, pady=10)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
button.config(padx=20, pady=10)

window.mainloop()