# import necessary classes from other modules
from hotel_booking import HotelBooking  
from room_selection import RoomSelection 

# function to open the room selection window
def open_room_selection_window(menu):

    hotel_booking = HotelBooking()  # create an instance of the hotel booking class
    room_selection = RoomSelection(menu, hotel_booking.update_selected_room)  # pass the menu and update function
    room_selection.open_room_selection_window()  # open the room selection window
