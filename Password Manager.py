from tkinter import *
from tkinter import messagebox
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list.append(random.choice(symbols)) 

for char in range(nr_numbers):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)

def password():
    password_entry.insert(0, password_list)
    
print(f"Your password is: {password}")

def save_password():
    if len(password_entry.get()) != 0 and len(email_entry.get()) > 5:
      
      ok = messagebox.askokcancel(title="Confirmation", message=f"These are the details entered:\nEmail/Username:{email_entry.get()}\nPassword:{password_entry.get()}\nWebsite:{website_entry.get()}\n Are these OK to save?")
      if ok: 
        with open("C:/Users/Basavaprabhu Ani/Desktop/passwords.txt", mode="a") as file:
            file.write(f"\n{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
      else:
        pass
    else:
      messagebox.showinfo(title="Oops", message="Please don't leave any fields empty. Retry")
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
# logo = PhotoImage(file="logo.png")
# canvas = Canvas(width=200, height=200)
# canvas.create_image(100, 100, image=logo)
# canvas.grid(row=0, column=1)
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "basavaprabhu.ani@gmail.com")
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)
generate_password_button = Button(text="Generate Password", command=password)
password_entry.config(textvariable=password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()