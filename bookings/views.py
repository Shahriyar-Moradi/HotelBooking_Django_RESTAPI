from drf_spectacular.utils import extend_schema
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from .models import Room, Booking, Hotel
from .serializers import RoomSerializer, BookingSerializer, HotelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework import generics
import rest_framework
from django.utils import timezone
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework import viewsets


# class GetRoomsByHotel(viewsets.ViewSet):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer
#     # lookup_field = "hotel_name"
#
#     # def retrieve(self, request, hotel_name):
#     #     serializer = RoomSerializer(self.queryset.filter(hotel__name=hotel_name), many=True)
#     #     #                                   .select_related('category','brand')
#     #     #                                   .prefetch_related(Prefetch('product_line'))
#     #     #                                   .prefetch_related(Prefetch('product_line__product_image'))
#     #     #                                   .prefetch_related(Prefetch('product_line__attribute_value__attribute'))
#     #     #                                   ,many=True)
#     #
#     #     data = Response(serializer.data)
#     #     return data
#
#     def create(self, request, *args, **kwargs):
#         # serializer = self.serializer_class(data=request.data)
#         # if serializer.is_valid(raise_exception=True):
#
#         hotel = request.data.get('hotel')
#         print("hotel",hotel)
#         hotel_name = Room.objects.get(hotel__name=hotel)
#         room_num = request.data.get('room_number')
#         print(room_num)
#         # hotel_name = hotel["hotel_name"]
#         print("hotel_name",hotel_name)
#
#             # Check if the desired room is available for booking at the specified time
#         existing_hotel = Hotel.objects.filter(name=hotel_name)
#         print(existing_hotel)
#         if existing_hotel.exists():
#             new_room = Room.objects.create(room_number=room_num,hotel=hotel)
#             new_room.save()
#
#             serializer = RoomSerializer(new_room)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         # return Response(serializer.errors, status=400)
#
class PostRoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


    def perform_create(self, serializer):
        room_num = serializer.validated_data['room_number']
        print("room_num",room_num)
        # hotel = request.data.get('hotel')
        hotel = serializer.validated_data['hotel_name']
        # hotel=hotels['name']
        print("hotel",hotel)


        # Check if the room is already booked for the given dates
        new_room = Room.objects.filter(
            room_number=room_num,
            hotel_name=hotel
        )
        if new_room.exists():
            raise serializers.ValidationError(f"Room {room_num} is already created for the specified Hotel {hotel}.")
        else:
            serializer.save()
            serializer = RoomSerializer()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

