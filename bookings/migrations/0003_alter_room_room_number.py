# Generated by Django 4.0.4 on 2023-08-02 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_remove_booking_user_booking_booked_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.IntegerField(),
        ),
    ]