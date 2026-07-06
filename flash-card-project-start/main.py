from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data_records = {}
new_word = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    data_records = original_data.to_dict(orient="records")
else:
    data_records = data.to_dict(orient="records")

def is_known():
    data_records.remove(new_word)
    df = pandas.DataFrame(data_records)
    df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(data_records)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(title_language, text="French", fill="black")
    canvas.itemconfig(card_word, text=new_word["French"], fill="black")
    flip_timer = window.after(3000, flip)

def flip():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(title_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=new_word["English"], fill="white")


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400,263,image=front_img)
title_language= canvas.create_text(400,150, text="", font=("Arial",40,"italic"))
card_word= canvas.create_text(400,263, text="", font=("Arial",60,"bold"))

canvas.grid(row=0,column=0, columnspan=2)

known_img = PhotoImage(file="./images/right.png")
unknown_img = PhotoImage(file="./images/wrong.png")

known_button = Button(image=known_img, highlightbackground=BACKGROUND_COLOR, command=is_known)
known_button.grid(row=1,column=1)

unknown_button = Button(image=unknown_img, highlightbackground=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=1,column=0)

flip_timer = window.after(3000, flip)
next_card()





window.mainloop()
