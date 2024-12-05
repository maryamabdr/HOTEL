import tkinter as tk
from tkinter import messagebox
import re
from datetime import datetime

def opensign(menu):
    user_data = {}

    bg_color = "#36335A"
    button_color = "#0b5394"
    hover_color = "#3d85c6"
    fg_color = "#ffffff"
    accent_color = "#9fc5e8"
    dark_blue = "#1e3c56"

    def open_menu():
        menu_window = tk.Toplevel()
        menu_window.title("Sign Up")
        menu_window.geometry("500x600")
        menu_window.configure(bg=bg_color)

        labels = ["Name", "Surname", "Email (Gmail)", "Credit Card Number", "Contact Number", "Birthday (YYYY-MM-DD)", "Password"]
        entries = {}

        for i, label in enumerate(labels):
            tk.Label(menu_window, text=label, bg=bg_color, fg=fg_color).grid(row=i, column=0, pady=10, padx=10, sticky="w")
            entry = tk.Entry(menu_window)
            entry.grid(row=i, column=1, pady=10, padx=10)
            entries[label] = entry

        entry_password = tk.Entry(menu_window, show="*")
        entries["Password"] = entry_password
        entry_password.grid(row=6, column=1, pady=10, padx=10)

        def validate_email(value):
            return re.match(r'^[a-zA-Z0-9_.+-]+@gmail\.com$', value)

        def validate_credit_card(value):
            return re.match(r'^\d{16}$', value)

        def validate_contact(value):
            return re.match(r'^\d{10}$', value)

        def validate_birthday(value):
            try:
                datetime.strptime(value, "%Y-%m-%d")
                return True
            except ValueError:
                return False

        def sign_up():
            name = entries["Name"].get()
            surname = entries["Surname"].get()
            email = entries["Email (Gmail)"].get()
            credit_card = entries["Credit Card Number"].get()
            contact = entries["Contact Number"].get()
            birthday = entries["Birthday (YYYY-MM-DD)"].get()
            password = entries["Password"].get()

            if not (name and surname and email and credit_card and contact and birthday and password):
                messagebox.showerror("Error", "All fields are required!")
                return

            if not validate_email(email):
                messagebox.showerror("Error", "Invalid Gmail address!")
                return

            if not validate_credit_card(credit_card):
                messagebox.showerror("Error", "Invalid credit card number!")
                return

            if not validate_contact(contact):
                messagebox.showerror("Error", "Invalid contact number!")
                return

            if not validate_birthday(birthday):
                messagebox.showerror("Error", "Invalid birthday format!")
                return

            if email in user_data:
                messagebox.showerror("Error", "User already exists!")
                return

            user_data[email] = {
                "name": name,
                "surname": surname,
                "email": email,
                "credit_card": credit_card,
                "contact": contact,
                "birthday": birthday,
                "password": password
            }

            messagebox.showinfo("Success", "Registration successful!")
            menu_window.destroy()

        submit_button = tk.Button(menu_window, text="Sign Up", command=sign_up, bg=button_color, fg=dark_blue, 
                                  activebackground=hover_color, activeforeground=fg_color, font=("Arial", 12))
        submit_button.grid(row=7, column=0, columnspan=2, pady=20)

    def open_login():
        login_window = tk.Toplevel()
        login_window.title("Log In")
        login_window.geometry("400x300")
        login_window.configure(bg=bg_color)

        tk.Label(login_window, text="Email (Gmail)", bg=bg_color, fg=fg_color).grid(row=0, column=0, pady=10, padx=10, sticky="w")
        tk.Label(login_window, text="Password", bg=bg_color, fg=fg_color).grid(row=1, column=0, pady=10, padx=10, sticky="w")

        entry_email = tk.Entry(login_window)
        entry_password = tk.Entry(login_window, show="*")

        entry_email.grid(row=0, column=1, pady=10, padx=10)
        entry_password.grid(row=1, column=1, pady=10, padx=10)

        def login():
            email = entry_email.get()
            password = entry_password.get()

            if email not in user_data:
                messagebox.showerror("Error", "User not found!")
                return

            if user_data[email]["password"] != password:
                messagebox.showerror("Error", "Incorrect password!")
                return

            messagebox.showinfo("Success", f"Welcome back, {user_data[email]['name']}!")
            login_window.destroy()

        login_button = tk.Button(login_window, text="Log In", command=login, bg=button_color, fg=dark_blue, 
                                 activebackground=hover_color, activeforeground=fg_color, font=("Arial", 12))
        login_button.grid(row=2, column=0, columnspan=2, pady=20)

    menu = tk.Tk()
    menu.geometry("600x400")
    menu.title("Main Application")
    menu.configure(bg=bg_color)

    sign_up_button = tk.Button(menu, text="Sign Up", command=open_menu, bg=button_color, fg=dark_blue, 
                               activebackground=hover_color, activeforeground=fg_color, font=("Arial", 14))
    sign_up_button.pack(pady=20)

    log_in_button = tk.Button(menu, text="Log In", command=open_login, bg=button_color, fg=dark_blue, 
                              activebackground=hover_color, activeforeground=fg_color, font=("Arial", 14))
    log_in_button.pack(pady=20)

    menu.mainloop()
