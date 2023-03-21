import pandas
import random
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
next_word = {}
to_learn = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# Words generation
def new_word():
    global next_word, flip_timer
    window.after_cancel(flip_timer)
    next_word = random.choice(to_learn)
    french_word = next_word["French"]
    canvas.itemconfig(card_image, image=front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    flip_timer = window.after(3000, func=flip_card)


# Flip card
def flip_card():
    english_word = next_word["English"]
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")


def word_known():
    to_learn.remove(next_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_word()


# User Interface (UI)
window = Tk()
window.title("Flashy")
window.config(pady=20, padx=20, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas()
canvas.config(width=800, height=526, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR)
back_image = PhotoImage(file="./images/card_back.png")
front_image = PhotoImage(file="./images/card_front.png")
card_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
button_right = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=word_known)
button_right.grid(row=1, column=0)
wrong_image = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=new_word)
button_wrong.grid(row=1, column=1)

new_word()

window.mainloop()


