from tkinter import *

window = Tk()

window.title("My GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="This is a Label", font=("Calibre", 25, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text Again")
my_label.grid(column=0, row= 0)
my_label.config(padx=20, pady=20)


# Button
def button_clicked():
    print("I got clicked")
    user_input = input.get()
    my_label.config(text=user_input)

button = Button(text= "First Button", command= button_clicked)
button.grid(column= 1, row= 1)

button2 = Button(text="Second Button")
button2.grid(column= 2,row =0)

# Entry
input = Entry(width=10)
input.grid(column= 3, row=2)



window.mainloop()

