# 15 36
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

is_equal_label =Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

miles_label =Label(text="Miles")
miles_label.grid(column=2, row=0)

kilometers_result_label =Label(text="0")
kilometers_result_label.grid(column=1, row=1)

kilometers_label =Label(text="Km")
kilometers_label.grid(column=2, row=1)

user_input = Entry(width=7)
user_input.grid(column=1, row=0)

def convert():
    miles = float(user_input.get())
    km = round((miles * 1.60934), 2)
    kilometers_result_label.config(text=f"{km}")

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)






window.mainloop()