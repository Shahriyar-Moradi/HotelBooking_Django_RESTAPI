from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    room_number = models.IntegerField()
    hotel_name = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    # def __str__(self):
    #     return str(self.room_number)

    # def __init__(self, room_num):
    #     self.room_number = room_num
    #
    def __str__(self):
        # return str(self.room_number)
        return f"Room {self.room_number} in {self.hotel_name}"


class Booking(models.Model):
    room = models.ForeignKey(Room, models.CASCADE)
    booked_name = models.CharField(max_length=200,blank=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return str(self.booked_name)
