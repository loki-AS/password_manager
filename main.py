from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    passwordBox.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = textbox1.get()
    email = textbox2.get()
    password = passwordBox.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOps!", message="Please don't have any fields empty!")
    else:
        try:
            with open("passwordManager.json", "r") as f:
                # json data
                data = json.load(f)
        except FileNotFoundError:
            with open("passwordManager.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)

            with open("passwordManager.json", "w") as f:
                # saving json data
                json.dump(data, f, indent=4)
        finally:
            textbox1.delete(0, END)
            passwordBox.delete(0, END)
            textbox1.focus()

# ---------------------------- searching password ------------------------------- #


def search_pass():
    website = textbox1.get()
    try:
        with open("passwordManager.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data File Found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \n password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No match found for {website}!")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

myCanvas = Canvas(width=200, height=200)
background_img = PhotoImage(file="logo.png")
myCanvas.create_image(100, 100, image=background_img)
myCanvas.grid(row=0, column=1)

label1 = Label(text="Website: ")
label1.grid(row=1, column=0)

label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)

label3 = Label(text="Password:")
label3.grid(row=3, column=0)

# entries

textbox1 = Entry(width=24)
print(textbox1.get())
textbox1.grid(row=1, column=1)
textbox1.focus()

textbox2 = Entry(width=42)
print(textbox2.get())
textbox2.grid(row=2, column=1, columnspan=2)
textbox2.insert(END, "lohith6617@gmail.com")

passwordBox = Entry(width=24)
print(passwordBox.get())
passwordBox.grid(row=3, column=1)

# Buttons

search_button = Button(text="Search", width=13, command=search_pass)
search_button.grid(row=1, column=2)

generatePass = Button(text="Generate Password", command=pass_generator)
generatePass.grid(row=3, column=2)

addPass = Button(text="Add", width=36, command=save_password)
addPass.grid(row=4, column=1, columnspan=2)

window.mainloop()