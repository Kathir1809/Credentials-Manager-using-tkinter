from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_let = [random.choice(letters) for item in range(nr_letters)]

password_sym = [random.choice(symbols) for it in range(nr_symbols)]

password_num = [random.choice(numbers) for ite in range(nr_numbers)]

password_list = password_num + password_sym + password_let

random.shuffle(password_list)

password = "".join(password_list)

# print(f"Your password is: {password}")


def pass_execute():
    global password
    i3.insert(0, password)
    window.clipboard_append(string=password)


def search():
    try:
        with open("data.json", mode="r") as d_f:
            data_file = json.load(d_f)

        website = i1.get()
        if website in data_file:
                    email = data_file[website]["email"]
                    password_u = data_file[website]["pass"]
                    messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password_u}")

        elif website == "":
            messagebox.showinfo(title="Error", message=f"Enter website name to search")

        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} Found")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def execute():
    web = i1.get()
    user = i2.get()
    pas = i3.get()
    dic = {
        web: {
            "email": user,
            "pass": pas,
        }
    }
    save(web, user, pas, dic)


def save(a, b, c, d):
    if len(a) == 0 or len(b) == 0 or len(c) == 0:
        messagebox.showerror(title="Oops", message="Don't leave any field empty")
    else:
        is_ok = messagebox.askyesno(title=a, message=f"These are the details entered: \nEmail: {b} \nPassword: {c}")

        if is_ok:
            with open(file="dat.txt", mode="a") as fil:
                fil.write(f"{a} | {b} | {c}\n")

            try:
                with open(file="data.json", mode="r") as file:
                    dat = json.load(file)
                    dat.update(d)

            except:
                with open(file="data.json", mode="w") as file:
                    json.dump(d, file, indent=4)

            else:
                with open(file="data.json", mode="w") as file:
                    json.dump(dat, file, indent=4)

            finally:
                i1.delete(0, END)
                i3.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("My password manager")
window.config(padx=20, pady=20)
img = PhotoImage(file="logo.png")

canva = Canvas(width=200, height=200)
canva.create_image(100, 100, image=img)
canva.grid(column=1, row=0)

t1 = Label(text="Website:", font=("Arial", 10, "bold"))
t1.grid(column=0, row=1)

t2 = Label(text="Email/Username:", font=("Arial", 10, "bold"))
t2.grid(column=0, row=2)

t3 = Label(text="Password:", font=("Arial", 10, "bold"))
t3.grid(column=0, row=3)

i1 = Entry(width=21)
i1.grid(column=1, row=1)
i1.focus()

i2 = Entry(width=35)
i2.grid(column=1, row=2, columnspan=2)
i2.insert(0, "abc@gmail.com")

i3 = Entry(width=21)
i3.grid(column=1, row=3)

but1 = Button(text="Generate Password", command=pass_execute)
but1.grid(column=2, row=3)

but2 = Button(text="Add", width=36, command=execute)
but2.grid(column=1, row=4, columnspan=2)

but3 = Button(text="Search", width=14, command=search)
but3.grid(column=2, row=1)

window.mainloop()