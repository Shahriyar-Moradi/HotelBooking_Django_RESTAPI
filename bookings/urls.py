from django.contrib import admin
from django.urls import path, include

# from .views import HotelList,RoomList,BookingViewSet
# from .views import BookingViewSet,RoomViewSet,HotelViewSet
# from .views import RoomViewSet,HotelViewSet
from .views import HotelViewSet
# from .views import RoomCreateAPIView

from rest_framework import routers

from .views import PostRoomViewSet,RoomsByHotel

router = routers.DefaultRouter()
router.register(r'rooms', RoomsByHotel,basename='rooms_by_hotel')
# router.register(r'hotels', HotelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('hotels/<int:pk>/rooms/', HotelViewSet.as_view({'get': 'rooms'}), name='hotel-rooms'),
    path('hotels/', HotelViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='hotel_list'),
    # path('hotels/', HotelList.as_view(), name='hotel_list'),
    # path('rooms/', RoomList.as_view(), name='room_list'),
    # path('bookings/', BookingList.as_view(), name='booking_list'),
    # path('room/post/',  RoomCreateAPIView.as_view(), name='booking_list'),

    path('room/', PostRoomViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='room_list'),



]
