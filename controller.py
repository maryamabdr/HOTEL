from hotel_booking import HotelBooking  
from room_selection import RoomSelection 

def open_room_selection_window(menu):

    hotel_booking = HotelBooking()  
    room_selection = RoomSelection(menu, hotel_booking.update_selected_room)
    room_selection.open_room_selection_window()