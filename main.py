from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
FONT_NAME = "Arial"
# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search():
    website = entered_website.get().title()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}\n\nPassword Copied!")
            pyperclip.copy(password)
    except KeyError:
        messagebox.showerror(title="Error", message="Website does not exist")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entered_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(7, 9))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 3))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 3))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entered_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = entered_website.get().title()
    email = entered_email.get()
    password = entered_password.get()
    data_string = website + " | " + email + " | " + password
    new_data = {website:{
        "email": email,
        "password":password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please fill in all fields!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            entered_website.delete(0, END)
            entered_website.focus()
            entered_password.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50,pady=50, bg="white")
canvas = Canvas(width=200,height=200, bg="white", highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(55,100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME, 13, "bold"), bg="white")
website_label.grid(column=0, row=1, sticky="e")
entered_website = Entry(bg="white",width=20, font=(FONT_NAME, 11))
entered_website.grid(column=1, row=1, sticky="w")
entered_website.focus()

search_button = Button(text="Search", command=search, width=14)
search_button.grid(column=1, row=1, sticky="e")

email_label = Label(text="Email/Username:", font=(FONT_NAME, 13, "bold"), bg="white")
email_label.grid(column=0, row=2, sticky="e")
entered_email = Entry(bg="white", width=36, font=(FONT_NAME, 11))
entered_email.insert(0,"Kfausch@outlook.com")
entered_email.grid(column=1, row=2, sticky="s")

password_label = Label(text="Password:", font=(FONT_NAME, 13, "bold"), bg="white")
password_label.grid(column=0, row=3, sticky="e")
entered_password = Entry(bg="white", font=(FONT_NAME, 11))
entered_password.grid(column=1, row=3, sticky="w")

generate_passowrd = Button(text="Generate Password", command=generate_password)
generate_passowrd.grid(column=1, row=3, sticky="e")

add_button = Button(text="Add", width=40, command=save_data)
add_button.grid(column=1, row=5, sticky="n", pady=10)

window.mainloop()