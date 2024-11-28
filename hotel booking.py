from ast import main
import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
from room_selection import open_room_selection
from menu import open_menu
import subprocess
import os


def show_calendar(label):
    def select_date():
        selected_date = cal.selection_get()
        label.config(text=selected_date)
        calendar_window.destroy()

    calendar_window = tk.Toplevel(inner_frame)
    calendar_window.title("Select Date")
    cal = Calendar(calendar_window, selectmode="day")
    cal.pack(pady=20)
    select_button = tk.Button(calendar_window, text="Select", command=select_date)
    select_button.pack(pady=10)

def book_now():
    selected_destination = destination_var.get()
    if selected_destination == "Select Destination":
        messagebox.showwarning("Missing Info", "Please select a destination.")
    elif start_date_label.cget("text") == "Start Date":
        messagebox.showwarning("Missing Info", "Please select a check-in date.")
    elif end_date_label.cget("text") == "End Date":
        messagebox.showwarning("Missing Info", "Please select a check-out date.")
    else:
        messagebox.showinfo("Booking", f"Booking successful!\nDestination: {selected_destination}\nCheck-in: {start_date_label.cget('text')}\nCheck-out: {end_date_label.cget('text')}")

menu = tk.Tk()
menu.overrideredirect(True)  
menu.geometry("1000x700")

outer_frame = tk.Frame(menu, bg="#36335A", bd=0)
outer_frame.pack(fill="both", expand=True)

inner_frame = tk.Frame(outer_frame, bg="#C3A464", padx=10, pady=10)
inner_frame.pack(fill="both", expand=True, padx=5, pady=5)


def start_move(event):
    menu.x = event.x
    menu.y = event.y

def move_window(event):
    x = menu.winfo_pointerx() - menu.x
    y = menu.winfo_pointery() - menu.y
    menu.geometry(f"+{x}+{y}")

outer_frame.bind("<Button-1>", start_move)
outer_frame.bind("<B1-Motion>", move_window)

script_dir = os.path.dirname(__file__) 
image_path = os.path.join(script_dir, "exterior.jpeg")

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


title = tk.Label(inner_frame, text="Welcome to Marbella Hotel", font=("Helvetica", 28, "bold"), bg="#36335A", fg="#C3A464")
title.pack(pady=20)

subtitle = tk.Label(inner_frame, text="...", font=("Helvetica", 16), bg="#36335A", fg="#FDFEFE")
subtitle.pack(pady=10)

destination_frame = tk.Frame(inner_frame, bg="#36335A")
destination_frame.pack(pady=20)

destination_label = tk.Label(destination_frame, text="DESTINATION", font=("Arial", 10, "bold"), fg="black", bg="#36335A")
destination_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

style = ttk.Style()
style.theme_use("clam")
style.configure("Custom.TCombobox",
                fieldbackground="#36335A",  
                background="#36335A",      
                foreground="white",        
                arrowcolor="white",       
                bordercolor="#36335A")      

destination_var = tk.StringVar(value="Select Destination")
destination_combobox = ttk.Combobox(destination_frame, textvariable=destination_var, font=("Arial", 12), state="readonly", width=40, style="Custom.TCombobox")
destination_combobox["values"] = ["Dubai", "London", "Madrid", "New York", "Paris", "Rome"]
destination_combobox.grid(row=1, column=0, padx=10, pady=5)


date_frame = tk.Frame(inner_frame, bg="#C3A464")
date_frame.pack(pady=10)

start_date_label = tk.Label(date_frame, text="Start Date", font=("Arial", 12), bg="#C3A464", fg="black")
start_date_label.grid(row=0, column=0, padx=10, pady=5)

start_date_button = tk.Button(date_frame, text="Select Check-In", font=("Arial", 12), bg="#D5DBDB", command=lambda: show_calendar(start_date_label))
start_date_button.grid(row=1, column=0, padx=10, pady=5)

end_date_label = tk.Label(date_frame, text="End Date", font=("Arial", 12), bg="#C3A464", fg="black")
end_date_label.grid(row=0, column=1, padx=10, pady=5)

end_date_button = tk.Button(date_frame, text="Select Check-Out", font=("Arial", 12), bg="#D5DBDB", command=lambda: show_calendar(end_date_label))
end_date_button.grid(row=1, column=1, padx=10, pady=5)

btn_book = tk.Button(inner_frame, text="Book Now", font=("Helvetica", 14), bg="#F1C40F", fg="#2C3E50", activebackground="#D4AC0D", activeforeground="black", command=book_now)
btn_book.pack(pady=20, ipadx=20, ipady=10)

btn_details = tk.Button(inner_frame, text="View Details", font=("Helvetica", 14), bg="#ECF0F1", fg="#2C3E50", activebackground="#BDC3C7", activeforeground="black", command=lambda: messagebox.showinfo("Details", "Viewing hotel details."))
btn_details.pack(pady=10, ipadx=20, ipady=10)

close_button = tk.Button(outer_frame, text="Close", font=("Arial", 10, "bold"), bg="red", fg="#36335A", command=menu.destroy)
close_button.place(relx=1.0, rely=0.0, anchor="ne")

footer = tk.Label(inner_frame, text="© 2024 Marbella Hotel. All rights reserved.", font=("Helvetica", 10), bg="#2C3E50", fg="#BDC3C7")
footer.pack(side="bottom", pady=20)

sign_button = tk.Button(outer_frame, text="Sign", font=("Arial", 10, "bold"), bg="red", fg="#36335A", command=lambda: open_menu(menu))
sign_button.place(relx=0.95, rely=0.0, anchor="ne")

open_room_button = tk.Button(inner_frame, text="Open Room Selection", command=lambda: open_room_selection(menu))
open_room_button.pack(pady=20)

menu.mainloop()


