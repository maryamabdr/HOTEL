import tkinter as tk
from tkinter import messagebox
import re
from datetime import datetime

def opensign(menu):
    user_data = {}

    # Color scheme
    bg_color = "#073764"
    button_color = "#0b5394"
    hover_color = "#3d85c6"
    fg_color = "#ffffff"
    accent_color = "#9fc5e8"

    def open_menu():
        """Opens the sign-up window."""
        menu_window = tk.Toplevel()
        menu_window.title("Sign Up")
        menu_window.geometry("500x600")
        menu_window.configure(bg=bg_color)

        # Create labels and entry fields for sign up
        tk.Label(menu_window, text="Name", bg=bg_color, fg=fg_color).grid(row=0, column=0, pady=10, padx=10, sticky="w")
        tk.Label(menu_window, text="Surname", bg=bg_color, fg=fg_color).grid(row=1, column=0, pady=10, padx=10, sticky="w")
        tk.Label(menu_window, text="Email (Gmail)", bg=bg_color, fg=fg_color).grid(row=2, column=0, pady=10, padx=10, sticky="w")
        tk.Label(menu_window, text="Credit Card Number", bg=bg_color, fg=fg_color).grid(row=3, column=0, pady=10, padx=10, sticky="w")
        tk.Label(menu_window, text="Contact Number", bg=bg_color, fg=fg_color).grid(row=4, column=0, pady=10, padx=10, sticky="w")
        tk.Label(menu_window, text="Birthday (YYYY-MM-DD)", bg=bg_color, fg=fg_color).grid(row=5, column=0, pady=10, padx=10, sticky="w")
        tk.Label(menu_window, text="Password", bg=bg_color, fg=fg_color).grid(row=6, column=0, pady=10, padx=10, sticky="w")

        entry_name = tk.Entry(menu_window)
        entry_surname = tk.Entry(menu_window)
        entry_email = tk.Entry(menu_window)
        entry_credit_card = tk.Entry(menu_window)
        entry_contact = tk.Entry(menu_window)
        entry_birthday = tk.Entry(menu_window)
        entry_password = tk.Entry(menu_window, show="*")

        entry_name.grid(row=0, column=1, pady=10, padx=10)
        entry_surname.grid(row=1, column=1, pady=10, padx=10)
        entry_email.grid(row=2, column=1, pady=10, padx=10)
        entry_credit_card.grid(row=3, column=1, pady=10, padx=10)
        entry_contact.grid(row=4, column=1, pady=10, padx=10)
        entry_birthday.grid(row=5, column=1, pady=10, padx=10)
        entry_password.grid(row=6, column=1, pady=10, padx=10)

        # Sign-up function
        def validate_email(value):
            """Validates if the email is a Gmail address."""
            return re.match(r'^[a-zA-Z0-9_.+-]+@gmail\.com$', value)

        def validate_credit_card(value):
            """Validates if the credit card number has 16 digits."""
            return re.match(r'^\d{16}$', value)

        def validate_contact(value):
            """Validates if the contact number has 10 digits."""
            return re.match(r'^\d{10}$', value)

        def validate_birthday(value):
            """Validates if the birthday is in the format YYYY-MM-DD."""
            try:
                datetime.strptime(value, "%Y-%m-%d")
                return True
            except ValueError:
                return False

        def sign_up():
            """Handles user registration."""
            name = entry_name.get()
            surname = entry_surname.get()
            email = entry_email.get()
            credit_card = entry_credit_card.get()
            contact = entry_contact.get()
            birthday = entry_birthday.get()
            password = entry_password.get()

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

        # Submit button
        submit_button = tk.Button(menu_window, text="Sign Up", command=sign_up, bg=button_color, fg=fg_color)
        submit_button.grid(row=7, column=0, columnspan=2, pady=20)

    def open_login():
        """Opens the login window."""
        login_window = tk.Toplevel()
        login_window.title("Log In")
        login_window.geometry("400x300")
        login_window.configure(bg=bg_color)

        # Create labels and entry fields for login
        tk.Label(login_window, text="Email (Gmail)", bg=bg_color, fg=fg_color).grid(row=0, column=0, pady=10, padx=10, sticky="w")
        tk.Label(login_window, text="Password", bg=bg_color, fg=fg_color).grid(row=1, column=0, pady=10, padx=10, sticky="w")

        entry_email = tk.Entry(login_window)
        entry_password = tk.Entry(login_window, show="*")

        entry_email.grid(row=0, column=1, pady=10, padx=10)
        entry_password.grid(row=1, column=1, pady=10, padx=10)

        # Login function
        def login():
            """Handles user login."""
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

        # Login button
        login_button = tk.Button(login_window, text="Log In", command=login, bg=button_color, fg=fg_color)
        login_button.grid(row=2, column=0, columnspan=2, pady=20)

    # Main menu window
    menu = tk.Tk()
    menu.geometry("600x400")
    menu.title("Main Application")
    menu.configure(bg=bg_color)

    sign_up_button = tk.Button(menu, text="Sign Up", command=open_menu, bg=button_color, fg=fg_color, font=("Arial", 14))
    sign_up_button.pack(pady=20)

    log_in_button = tk.Button(menu, text="Log In", command=open_login, bg=button_color, fg=fg_color, font=("Arial", 14))
    log_in_button.pack(pady=20)

    menu.mainloop()
