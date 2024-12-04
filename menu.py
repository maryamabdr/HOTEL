
import re
import tkinter as tk
from tkinter import messagebox




def open_menu(menu):
    def validate_email(email):
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

    user_data = {}

    def sign_up():
        def save_user():
            name = entry_name.get()
            surname = entry_surname.get()
            dob = entry_dob.get()
            credit_card = entry_credit_card.get()
            password = entry_password.get()

            
            if not name or not surname or not dob or not credit_card or not password:
                messagebox.showerror("Error", "All fields are required!")
                return

            if not validate_email(credit_card): 
                messagebox.showerror("Error", "Invalid email or credit card!")
                return

            if name in user_data:
                messagebox.showerror("Error", "User already exists!")
                return

            user_data[name] = {
                "surname": surname,
                "dob": dob,
                "credit_card": credit_card,
                "password": password
            }

            messagebox.showinfo("Success", "Registration successful!")
            sign_up_window.destroy()

        sign_up_window = tk.Toplevel(menu)
        sign_up_window.title("Sign Up")

        tk.Label(sign_up_window, text="Name").grid(row=0, column=0)
        tk.Label(sign_up_window, text="Surname").grid(row=1, column=0)
        tk.Label(sign_up_window, text="Date of Birth (DD/MM/YYYY)").grid(row=2, column=0)
        tk.Label(sign_up_window, text="Email or Credit Card").grid(row=3, column=0)
        tk.Label(sign_up_window, text="Password").grid(row=4, column=0)

        entry_name = tk.Entry(sign_up_window)
        entry_surname = tk.Entry(sign_up_window)
        entry_dob = tk.Entry(sign_up_window)
        entry_credit_card = tk.Entry(sign_up_window)
        entry_password = tk.Entry(sign_up_window, show="*")

        entry_name.grid(row=0, column=1)
        entry_surname.grid(row=1, column=1)
        entry_dob.grid(row=2, column=1)
        entry_credit_card.grid(row=3, column=1)
        entry_password.grid(row=4, column=1)

        submit_button = tk.Button(sign_up_window, text="Sign Up", command=save_user)
        submit_button.grid(row=5, column=0, columnspan=2)

        sign_up_window.mainloop()
