import tkinter as tk
from tkinter import messagebox, ttk
import re

def opensign(menu):
    user_data = {}

    def open_menu():
        """Opens the sign-up window."""
        menu_window = tk.Toplevel()
        menu_window.title("Sign Up")
        menu_window.geometry("400x400")
        menu_window.configure(bg="#F0F0F0")

        def validate_email_or_credit_card(value):
            """Validates if the input is either an email or a credit card number."""
            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            credit_card_regex = r'^\d{16}$'  
            return re.match(email_regex, value) or re.match(credit_card_regex, value)

        def sign_up():
            """Handles user registration."""
            name = entry_name.get()
            email_or_cc = entry_email_or_cc.get()
            password = entry_password.get()

            if not name or not email_or_cc or not password:
                messagebox.showerror("Error", "All fields are required!")
                return

            if not validate_email_or_credit_card(email_or_cc):
                messagebox.showerror("Error", "Invalid email or credit card!")
                return

            if email_or_cc in user_data:
                messagebox.showerror("Error", "User already exists!")
                return

            user_data[email_or_cc] = {
                "name": name,
                "password": password
            }

            messagebox.showinfo("Success", "Registration successful!")
            menu_window.destroy()

        
            tk.Label(menu_window, text="Name").grid(row=0, column=0, pady=10, padx=10, sticky="w")
            tk.Label(menu_window, text="Email or Credit Card").grid(row=1, column=0, pady=10, padx=10, sticky="w")
            tk.Label(menu_window, text="Password").grid(row=2, column=0, pady=10, padx=10, sticky="w")

            entry_name = tk.Entry(menu_window)
            entry_email_or_cc = tk.Entry(menu_window)
            entry_password = tk.Entry(menu_window, show="*")

            entry_name.grid(row=0, column=1, pady=10, padx=10)
            entry_email_or_cc.grid(row=1, column=1, pady=10, padx=10)
            entry_password.grid(row=2, column=1, pady=10, padx=10)

            submit_button = tk.Button(menu_window, text="Sign Up", command=sign_up, bg="#0078D4", fg="white")
            submit_button.grid(row=3, column=0, columnspan=2, pady=20)

    def open_login():
        """Opens the login window."""
        login_window = tk.Toplevel()
        login_window.title("Log In")
        login_window.geometry("400x300")
        login_window.configure(bg="#F0F0F0")

        def login():
            """Handles user login."""
            email_or_cc = entry_email_or_cc.get()
            password = entry_password.get()

            if email_or_cc not in user_data:
                messagebox.showerror("Error", "User not found!")
                return

            if user_data[email_or_cc]["password"] != password:
                messagebox.showerror("Error", "Incorrect password!")
                return

            messagebox.showinfo("Success", f"Welcome back, {user_data[email_or_cc]['name']}!")
            login_window.destroy()

        # Login form widgets
        tk.Label(login_window, text="Email or Credit Card").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        tk.Label(login_window, text="Password").grid(row=1, column=0, pady=10, padx=10, sticky="w")

        entry_email_or_cc = tk.Entry(login_window)
        entry_password = tk.Entry(login_window, show="*")

        entry_email_or_cc.grid(row=0, column=1, pady=10, padx=10)
        entry_password.grid(row=1, column=1, pady=10, padx=10)

        login_button = tk.Button(login_window, text="Log In", command=login, bg="#28B463", fg="white")
        login_button.grid(row=2, column=0, columnspan=2, pady=20)


    menu = tk.Tk()
    menu.geometry("600x400")
    menu.title("Main Application")


    sign_up_button = tk.Button(menu, text="Sign Up", command=open_menu, bg="#0078D4", fg="white", font=("Arial", 14))
    sign_up_button.pack(pady=20)

    log_in_button = tk.Button(menu, text="Log In", command=open_login, bg="#28B463", fg="white", font=("Arial", 14))
    log_in_button.pack(pady=20)

    menu.mainloop()
