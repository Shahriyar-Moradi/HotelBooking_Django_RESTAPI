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
from django.shortcuts import render, get_object_or_404


class RoomsByHotel(viewsets.ViewSet):
    def list_comment_by_post(self, request, hotel_id):
        hotel = get_object_or_404(Hotel, id=hotel_id)
        rooms = Room.objects.filter(hotel=hotel)
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
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

    @extend_schema(
        description="Retrieve a list of objects",  # Provide a description
        responses=HotelSerializer(many=True),
        methods=["GET"],  # Customize the HTTP methods for this view
    )
    def rooms(self, request, pk=None):
        hotel = self.get_object()
        rooms = Room.objects.filter(hotel_name=hotel)
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

