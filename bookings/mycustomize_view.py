from drf_spectacular.utils import extend_schema
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from .models import Room, Booking, Hotel
from .serializers import RoomSerializer, BookingSerializer, HotelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import rest_framework

from rest_framework.decorators import api_view, renderer_classes, action


class HotelList(APIView):
    @extend_schema(request=None, responses=HotelSerializer)
    def get(self, request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = BookSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST


class RoomList(APIView):
    @extend_schema(request=None, responses=RoomSerializer)
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)


# class BookingList(APIView):
#     booking_list = Booking.objects.all()
#     serializer_class = BookingSerializer
#
#     def perform_create(self, serializer):
#         room = serializer.validated_data['room']
#         check_in = serializer.validated_data['check_in']
#         check_out = serializer.validated_data['check_out']
#
#         # Check if the room is already booked for the given dates
#         bookings = Booking.objects.filter(
#             room=room,
#             check_in__lt=check_out,
#             check_out__gt=check_in
#         )
#         if bookings.exists():
#             raise serializers.ValidationError("Room is already booked for the specified dates.")
#
#         serializer.save(user=self.request.user)

# class BookingList(APIView):
#     def post(self, request):
#         serializer = BookingSerializer(data=request.data)
#         if serializer.is_valid():
#             # room = serializer.validated_data['room']
#             # check_in_date = serializer.validated_data['check_in_date']
#             # check_out_date = serializer.validated_data['check_out_date']
#
#                     # Check if the room is already booked for the given dates
#             # bookings = Booking.objects.filter(
#             #     room=room,
#             #     check_in__lt=check_in_date,
#             #     check_out__gt=check_out_date
#             # )
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#             # if bookings.exists():
#             #     raise serializers.ValidationError("Room is already booked for the specified dates.")
#             # serializer.save(user=self.request.user)
#         #
#         # serializer = BookingSerializer(data=request.data)
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from drf_spectacular.utils import extend_schema, OpenApiExample, inline_serializer
class BookingList(APIView):

    serializer_class =BookingSerializer
    # serializer_class = serializers.BookingSerializer
    # serializer_class = rest_framework.serializers.Serializer
    #
    @extend_schema(request=None, responses=BookingSerializer)
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)




    #
    #     # @swagger_auto_schema(method='post', request_body=BookingSerializer)
    #     # @action(methods=['post'], detail=False)
    #     # @api_view(['post'])
    #     # @api_view(['POST'])




    # @extend_schema(description='Override a specific method', methods=["POST"])
    @action(detail=True, methods=["POST"])
    def post(self, request):
        # bookings = Booking.objects.all()
        # data = request.data
        serialized_data = BookingSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def post_booking(request):
#     serialized_data = BookingSerializer(data=request.data,many=True)
#     if serialized_data.is_valid():
#         serialized_data.save()
#         return Response(serialized_data.data, status=status.HTTP_201_CREATED)
#     return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def books_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Booking.objects.all()
#         serializer = BookingSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = BookingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)