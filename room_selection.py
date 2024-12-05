import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import os

class RoomSelection:
    def __init__(self, menu, update_selected_room):
        self.menu = menu
        self.update_selected_room = update_selected_room

    def open_room_selection_window(self):
    
        room_selection_window = tk.Toplevel(self.menu)
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

        rooms = [                                   #room info
            ("Single Room", "1 Person", 80, 90),
            ("Twin Room", "2 People", 120, 140),
            ("Double Room", "2 People", 160, 180),
            ("Triple Room", "3 People", 200, 220),
            ("Deluxe Room", "2-3 People", 250, 270),
            ("Suite", "Up to 4 People", 350, 370)
        ]

        room_images = ["single room.jpeg", "twin room.jpeg", "double room.jpeg", "triple room.jpeg", "deluxe room.jpeg", "suite.jpeg.webp"]

        for i, room in enumerate(rooms):
            room_name, capacity, member_price, flexible_price = room
            room_image_path = os.path.join(os.getcwd(), room_images[i])

            room_frame = tk.Frame(inner_frame, bg="#36335A", padx=10, pady=10)
            room_frame.grid(row=i, column=0, padx=10, pady=20, sticky="nsew")

            try:
                room_img = Image.open(room_image_path)          #open image
                room_img = room_img.resize((200, 150), Image.Resampling.LANCZOS)  
                room_img = ImageTk.PhotoImage(room_img) 

                img_label = Label(room_frame, image=room_img)
                img_label.image = room_img  
                img_label.grid(row=0, column=0, rowspan=4, padx=10, pady=10)
            except Exception as e:                  #in case of failure
                img_label = Label(room_frame, text="Image Not Found", bg="gray", width=50, height=15)
                img_label.grid(row=0, column=0, rowspan=4, padx=10, pady=10)

            title_label = Label(room_frame, text=room_name, font=("Arial", 16, "bold"), fg="white", bg="#36335A")
            title_label.grid(row=0, column=1, sticky="w", padx=10)

            details_label = Label(room_frame, text=f"Capacity: {capacity}", font=("Arial", 12), fg="white", bg="#36335A")
            details_label.grid(row=1, column=1, sticky="w", padx=10)

            member_rate_label = Label(room_frame, text="Member Rate:", font=("Arial", 12, "bold"), fg="white", bg="#36335A")
            member_rate_label.grid(row=2, column=1, sticky="w", padx=10)
            member_price_label = Label(room_frame, text=f"€{member_price} / NIGHT", font=("Arial", 12), fg="white", bg="#36335A")
            member_price_label.grid(row=2, column=2, sticky="e", padx=10)

            flexible_rate_label = Label(room_frame, text="Non-Member Rate:", font=("Arial", 12, "bold"), fg="white", bg="#36335A")
            flexible_rate_label.grid(row=3, column=1, sticky="w", padx=10)
            flexible_price_label = Label(room_frame, text=f"€{flexible_price} / NIGHT", font=("Arial", 12), fg="white", bg="#36335A")
            flexible_price_label.grid(row=3, column=2, sticky="e", padx=10) #prices

            member_button = Button(room_frame, text="Select", font=("Arial", 14, "bold"), fg="#F1C40F", width=15, height=2, relief="flat", 
                                   command=lambda room_name=room_name, price=member_price: self.update_selected_room(room_name, price))
            member_button.grid(row=2, column=3, padx=10)

            flexible_button = Button(room_frame, text="Select", font=("Arial", 14, "bold"), fg="#F1C40F", width=15, height=2, relief="flat", 
                                     command=lambda room_name=room_name, price=flexible_price: self.update_selected_room(room_name, price))
            flexible_button.grid(row=3, column=3, padx=10) #buttons selecting the room

        inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        room_selection_window.mainloop()
