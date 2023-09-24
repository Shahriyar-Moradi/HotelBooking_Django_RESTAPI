from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Room, Booking, Hotel
from rest_framework import serializers

from drf_writable_nested import WritableNestedModelSerializer
class HotelSerializer(serializers.ModelSerializer):

    hotel_name=serializers.CharField(source='name')

    class Meta:
        model = Hotel
        # fields = ['name']
        fields = ['id','hotel_name']
        # fields = '__all__'


class RoomSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):

    # room_num=serializers.IntegerField(source='room_number')
    # HotelName= serializers.CharField(source="hotel_name.name")
    HotelName = serializers.CharField(source="hotel_name",read_only=True)
    # name= HotelSerializer(read_only=True)
    #####################################
    # hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())
    # model_b_ids = serializers.IntegerField(write_only=True)

    class Meta:
        model = Room
        # fields = '__all__'

        fields = ['id','room_number','hotel_name','HotelName']
        # fields = ['id','room_number','hotel_name']
        # read_only_fields = ('id','room_number','HotelName')



class BookingSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    room = RoomSerializer(many=True)
    # room_number = serializers.CharField(source="room.room_number")

    # def create(self, validated_data):
    #     return Booking.objects.create(**validated_data)

    class Meta:
        model = Booking
        # fields = '__all__'
        fields = ['check_in_date', 'check_out_date', 'room', 'booked_name']
        # fields = ['id', 'check_in_date', 'check_out_date', 'room', 'booked_name']
