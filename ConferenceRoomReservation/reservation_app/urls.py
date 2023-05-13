from django.urls import path
from . import views as reservation_views

app_name = 'reservation_app'

urlpatterns = [
    path('home/', reservation_views.home_view, name="home"),
    path('room/new/', reservation_views.AddRoomView.as_view(), name="add-room"),
    path('', reservation_views.RoomListView.as_view(), name="room-list"),
    path('room/delete/<int:room_id>/', reservation_views.DeleteRoomView.as_view(), name="delete-room"),
    path('room/modify/<int:room_id>/', reservation_views.ModifyRoomView.as_view(), name="modify-room"),
    path('room/book/<int:room_id>/', reservation_views.ReservationView.as_view(), name="book-room"),
    path('room/<int:room_id>/', reservation_views.RoomDetailsView.as_view(), name="room"),
    path('search/', reservation_views.SearchView.as_view(), name="room-list"),

]
