import tkinter as tk
from tkinter import Label, Button, PhotoImage
import os

def open_room_selection(menu):
    room_selection_window = tk.Toplevel(menu)
    room_selection_window.title("Room Selection")
    room_selection_window.geometry("900x600")

    outer_frame = tk.Frame(room_selection_window, bg="#C3A464")
    outer_frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(outer_frame)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(outer_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    inner_frame = tk.Frame(canvas, bg="#C3A464", padx=10, pady=10)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    rooms = [
        ("Single Room", "1 Person", 80, 90),
        ("Twin Room", "2 People", 120, 140),
        ("Double Room", "2 People", 160, 180),
        ("Triple Room", "3 People", 200, 220),
        ("Deluxe Room", "2-3 People", 250, 270),
        ("Suite", "Up to 4 People", 350, 370)
    ]

    room_images = ["single_room.jpg", "twin_room.jpg", "double_room.jpg", "triple_room.jpg", "deluxe_room.jpg", "suite_room.jpg"]

    for i, room in enumerate(rooms):
        room_name, capacity, member_price, flexible_price = room
        room_image_path = os.path.join(os.getcwd(), room_images[i])  # Update with current directory

        room_frame = tk.Frame(inner_frame, bg="#36335A", padx=10, pady=10)
        room_frame.grid(row=i, column=0, padx=10, pady=20, sticky="nsew")

        try:
            room_img = PhotoImage(file=room_image_path)
            img_label = Label(room_frame, image=room_img)
            img_label.image = room_img
            img_label.grid(row=0, column=0, rowspan=4, padx=10, pady=10)
        except Exception as e:
            img_label = Label(room_frame, text="Image Not Found", bg="gray", width=50, height=15)
            img_label.grid(row=0, column=0, rowspan=4, padx=10, pady=10)

        title_label = Label(room_frame, text=room_name, font=("Arial", 16, "bold"), fg="white", bg="#36335A")
        title_label.grid(row=0, column=1, sticky="w", padx=10)

        details_label = Label(room_frame, text=f"Capacity: {capacity}", font=("Arial", 12), fg="white", bg="#36335A")
        details_label.grid(row=1, column=1, sticky="w", padx=10)

        member_rate_label = Label(room_frame, text="Member Rate:", font=("Arial", 12, "bold"), fg="white", bg="#36335A")
        member_rate_label.grid(row=2, column=1, sticky="w", padx=10)
        member_price_label = Label(room_frame, text="€80 / NIGHT", font=("Arial", 12), fg="white", bg="#36335A")
        member_price_label.grid(row=2, column=2, sticky="e", padx=10)

        flexible_rate_label = Label(room_frame, text="Flexible Rate:", font=("Arial", 12, "bold"), fg="white", bg="#36335A")
        flexible_rate_label.grid(row=3, column=1, sticky="w", padx=10)
        flexible_price_label = Label(room_frame, text="€90 / NIGHT", font=("Arial", 12), fg="white", bg="#36335A")
        flexible_price_label.grid(row=3, column=2, sticky="e", padx=10)

        member_button = Button(room_frame, text="Select", font=("Arial", 12), bg="#0b5394", fg="white", width=10)
        member_button.grid(row=2, column=3, padx=10)

        flexible_button = Button(room_frame, text="Select", font=("Arial", 12), bg="#0b5394", fg="white", width=10)
        flexible_button.grid(row=3, column=3, padx=10)

    inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    
    room_selection_window.mainloop()
