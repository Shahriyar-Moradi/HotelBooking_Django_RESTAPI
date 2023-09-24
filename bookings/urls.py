from django.contrib import admin
from django.urls import path, include

# from .views import HotelList,RoomList,BookingViewSet
# from .views import BookingViewSet,RoomViewSet,HotelViewSet
# from .views import RoomViewSet,HotelViewSet
from .views import HotelViewSet
# from .views import RoomCreateAPIView

from rest_framework import routers
# from .views import GetRoomsByHotel
from .views import PostRoomViewSet

router = routers.DefaultRouter()
# router.register(r'rooms', GetRoomsByHotel)

urlpatterns = [
    path('', include(router.urls)),
    # path('hotels/', HotelList.as_view(), name='hotel_list'),
    # path('rooms/', RoomList.as_view(), name='room_list'),
    # path('bookings/', BookingList.as_view(), name='booking_list'),
    # path('room/post/',  RoomCreateAPIView.as_view(), name='booking_list'),
    path('hotels/', HotelViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='hotel_list'),

    path('room/', PostRoomViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='room_list'),

    # path('bookings/', BookingViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # }), name='booking_list'),
    # path('bookings/post', post_booking, name='booking_post'),
    # path('bookings/post', books_list, name='books_list'),

]
