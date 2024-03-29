from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    input_password.insert(0, f"{password}")

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_entries():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website == "" or password == "":
        messagebox.showinfo(title="Oops!",  message="Please don't leave website or email fields empty!")
    else:
        try:
            with open(file="data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open(file="data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)


# ---------------------------- Find Password ------------------------------- #
def find_password():
    website = input_website.get()
    try:
        with open(file="data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"email: {data[website]['email']}\n"
                                                       f"password: {data[website]['password']}")
            pyperclip.copy(data[website]["password"])
        else:
            messagebox.showinfo(title="Oops", message="This website is not in your list!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
my_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_image)
canvas.grid(row=0, column=1)

# Labels
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

# Entries
input_website = Entry(width=32)
input_website.grid(row=1, column=1)
input_website.focus()
input_email = Entry(width=52)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0, "email@hotmail.com")
input_password = Entry(width=32)
input_password.grid(row=3, column=1)

# Buttons
button_search = Button(text="Search", command=find_password, width=15)
button_search.grid(row=1, column=2)
button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2)
button_add = Button(text="Add", width=44, command=save_entries)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
