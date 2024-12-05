import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
from signlog import opensign
from room_selection import open_room_selection
import os
from datetime import datetime


# Function to show the calendar for selecting dates
def show_calendar(label, date_type):
    def select_date():
        selected_date = cal.selection_get()
        label.config(text=selected_date)
        
        if date_type == 'start':
            start_date_label.config(text=selected_date)
        elif date_type == 'end':
            end_date_label.config(text=selected_date)
        
        calendar_window.destroy()

    calendar_window = tk.Toplevel(inner_frame)
    calendar_window.title("Select Date")
    cal = Calendar(calendar_window, selectmode="day")
    cal.pack(pady=20)
    select_button = tk.Button(calendar_window, text="Select", command=select_date)
    select_button.pack(pady=10)



# Function to calculate the number of days stayed
def calculate_days():
    start_date_str = start_date_label.cget("text")
    end_date_str = end_date_label.cget("text")
    
    if start_date_str == "Start Date" or end_date_str == "End Date":
        return None
    
    try:
        # Parsing dates in the correct format (yyyy-mm-dd)
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        
        # Ensure that the check-out date is later than the check-in date
        if end_date <= start_date:
            return None
        
        return (end_date - start_date).days
    except ValueError:
        return None

# Function to handle the booking
def book_now():
    selected_destination = destination_var.get()
    
    if selected_destination == "Select Destination":
        messagebox.showwarning("Missing Info", "Please select a destination.")
    elif start_date_label.cget("text") == "Start Date":
        messagebox.showwarning("Missing Info", "Please select a check-in date.")
    elif end_date_label.cget("text") == "End Date":
        messagebox.showwarning("Missing Info", "Please select a check-out date.")
    else:
        days_stayed = calculate_days()
        if days_stayed is None or days_stayed <= 0:
            messagebox.showwarning("Invalid Dates", "Please make sure the check-out date is later than the check-in date.")
        else:
            messagebox.showinfo("Booking", f"Booking successful!\nDestination: {selected_destination}\nCheck-in: {start_date_label.cget('text')}\nCheck-out: {end_date_label.cget('text')}\nTotal Days: {days_stayed} days")

# Creating the main menu window
menu = tk.Tk()
menu.overrideredirect(True)
menu.geometry("1000x700")

outer_frame = tk.Frame(menu, bg="#36335A", bd=0)  
outer_frame.pack(fill="both", expand=True)

inner_frame = tk.Frame(outer_frame, bg="#C3A464", padx=10, pady=10)
inner_frame.pack(fill="both", expand=True, padx=5, pady=5)

script_dir = os.path.dirname(__file__) 
image_path = os.path.join(script_dir, "exterior.jpeg")

# Background image setup
try:
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((1000, 700), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(inner_frame, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
except Exception as e:
    print(f"Error loading image: {e}")
    bg_label = tk.Label(inner_frame, text="Background Image Not Found", bg="gray", font=("Arial", 20))
    bg_label.place(relwidth=1, relheight=1)

# Allow window dragging
def start_move(event):
    menu.x = event.x
    menu.y = event.y

def move_window(event):
    x = menu.winfo_pointerx() - menu.x
    y = menu.winfo_pointery() - menu.y
    menu.geometry(f"+{x}+{y}")

outer_frame.bind("<Button-1>", start_move)
outer_frame.bind("<B1-Motion>", move_window)

# Header labels
title = tk.Label(inner_frame, text="Welcome to Marbella Hotel", font=("Helvetica", 28, "bold"), bg="#36335A", fg="#C3A464")
title.pack(pady=20)

subtitle = tk.Label(inner_frame, text="The Gold Standard", font=("Helvetica", 18, "italic"), bg="#36335A", fg="#C3A464")
subtitle.pack(pady=10)

# Destination selection
destination_frame = tk.Frame(inner_frame, bg="#36335A")
destination_frame.pack(pady=20)

destination_label = tk.Label(destination_frame, text="Where would you like to stay?", font=("Arial", 12, "bold"), fg="black", bg="#36335A")
destination_label.grid(row=0, column=0, padx=10, pady=5)

style = ttk.Style()
style.theme_use("clam")
style.configure("Custom.TCombobox", fieldbackground="#36335A", background="#36335A", foreground="white", arrowcolor="white", bordercolor="#36335A")      

destination_var = tk.StringVar(value="Select Destination")
destination_combobox = ttk.Combobox(destination_frame, textvariable=destination_var, font=("Arial", 12), state="readonly", width=40, style="Custom.TCombobox")
destination_combobox["values"] = ["Dubai", "London", "Madrid", "New York", "Paris", "Rome"]
destination_combobox.grid(row=1, column=0, padx=10, pady=5)

# Date selection
date_frame = tk.Frame(inner_frame, bg="#C3A464")
date_frame.pack(pady=10)

start_date_label = tk.Label(date_frame, text="Check-in Date", font=("Arial", 12), bg="#C3A464", fg="black")
start_date_label.grid(row=0, column=0, padx=10, pady=5)

start_date_button = tk.Button(date_frame, text="Select Check-In", font=("Arial", 12), bg="#D5DBDB", command=lambda: show_calendar(start_date_label, 'start'))
start_date_button.grid(row=1, column=0, padx=10, pady=5)

end_date_label = tk.Label(date_frame, text="Check-out Date", font=("Arial", 12), bg="#C3A464", fg="black")
end_date_label.grid(row=0, column=1, padx=10, pady=5)

end_date_button = tk.Button(date_frame, text="Select Check-Out", font=("Arial", 12), bg="#D5DBDB", command=lambda: show_calendar(end_date_label, 'end'))
end_date_button.grid(row=1, column=1, padx=10, pady=5)

# Buttons to reserve and explore rooms
btn_book = tk.Button(inner_frame, text="Reserve Your Stay", font=("Helvetica", 16, "bold"), bg="#F1C40F", fg="#2C3E50", activebackground="#D4AC0D", activeforeground="black", command=book_now)
btn_book.pack(pady=30, ipadx=30, ipady=15)

btn_room_info = tk.Button(inner_frame, text="Explore Our Rooms", font=("Helvetica", 16, "bold"), bg="#ECF0F1", fg="#2C3E50", activebackground="#BDC3C7", activeforeground="black",  command=lambda: open_room_selection(menu))
btn_room_info.pack(pady=20, ipadx=30, ipady=15)

btn_special_offers = tk.Button(inner_frame, text="Special Offers", font=("Helvetica", 16, "bold"), bg="#ECF0F1", fg="#2C3E50", activebackground="#BDC3C7", activeforeground="black", command=lambda: messagebox.showinfo("Special Offers", "Check out our exclusive discounts and packages."))
btn_special_offers.pack(pady=20, ipadx=30, ipady=15)

# Footer
footer = tk.Label(inner_frame, text="© 2024 Marbella Hotel | All rights reserved.", font=("Helvetica", 10), bg="#2C3E50", fg="#BDC3C7")
footer.pack(side="bottom", pady=20)

# Close and Sign-in buttons
close_button = tk.Button(outer_frame, text="Close", font=("Arial", 10, "bold"), bg="red", fg="#36335A", command=menu.destroy)
close_button.place(relx=1.0, rely=0.0, anchor="ne")

sign_button = tk.Button(outer_frame, text="Sign In / Log In", font=("Arial", 10, "bold"), bg="red", fg="#36335A", command=lambda: opensign(menu))
sign_button.place(relx=0.935, rely=0.0, anchor="ne")

menu.mainloop()
