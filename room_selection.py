import tkinter as tk
from tkinter import Label, Button, PhotoImage

def open_room_selection(menu):
    room_selection_window = tk.Toplevel(menu)
    room_selection_window.title("Room Selection")
    room_selection_window.geometry("800x400")

    image_path = "your_image.png" 
    try:
        room_image = PhotoImage(file=image_path)
        img_label = Label(room_selection_window, image=room_image)
        img_label.image = room_image  
        img_label.grid(row=0, column=0, rowspan=4, padx=10, pady=10)
    except Exception as e:
        print(f"Error loading image: {e}")
        img_label = Label(room_selection_window, text="[Image Placeholder]", bg="gray", width=50, height=15)
        img_label.grid(row=0, column=0, rowspan=4, padx=10, pady=10)

    title_label = Label(room_selection_window, text="Club Ocean Twin Room, Club Level", font=("Arial", 16, "bold"))
    title_label.grid(row=0, column=1, sticky="w", padx=10)

    details_label = Label(room_selection_window, text="Guest room, 2 Queen, Ocean view, High floor, Balcony", font=("Arial", 12))
    details_label.grid(row=1, column=1, sticky="w", padx=10)

    member_rate_label = Label(room_selection_window, text="Member Rate Flexible:", font=("Arial", 12, "bold"))
    member_rate_label.grid(row=2, column=1, sticky="w", padx=10)
    member_price_label = Label(room_selection_window, text="5,194 AED / NIGHT", font=("Arial", 12))
    member_price_label.grid(row=2, column=2, sticky="e", padx=10)

    flexible_rate_label = Label(room_selection_window, text="Flexible Rate:", font=("Arial", 12, "bold"))
    flexible_rate_label.grid(row=3, column=1, sticky="w", padx=10)
    flexible_price_label = Label(room_selection_window, text="5,300 AED / NIGHT", font=("Arial", 12))
    flexible_price_label.grid(row=3, column=2, sticky="e", padx=10)

    member_button = Button(room_selection_window, text="Select", font=("Arial", 12), bg="black", fg="white", width=10)
    member_button.grid(row=2, column=3, padx=10)

    flexible_button = Button(room_selection_window, text="Select", font=("Arial", 12), bg="black", fg="white", width=10)
    flexible_button.grid(row=3, column=3, padx=10)
