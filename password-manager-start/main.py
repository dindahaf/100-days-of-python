from tkinter import *
from tkinter import messagebox
from random import randint, choice,shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_list += [choice(letters) for _ in range(nr_letters)]
    password_list += [choice(symbols) for _ in range(nr_symbols)]
    password_list += [choice(numbers) for _ in range(nr_numbers)]

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    user_website = website_input.get()
    user_username = username_input.get()
    user_password = password_input.get()

    if len(user_website) == 0 or len(user_password) == 0:
        messagebox.showinfo(message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(message=f"These are the details entered:\nWebsite: user_website\nEmail/Username: {user_username}\nPassword: {user_password}\nIs it Ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{user_website} | {user_username} | {user_password}\n")

            website_input.delete(0, END)
            password_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
logo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100,100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=38)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()


username_input = Entry(width=38)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0,"dinda@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1)


generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)













window.mainloop()