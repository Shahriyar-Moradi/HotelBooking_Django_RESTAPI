# Generated by Django 4.0.4 on 2023-08-02 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_alter_room_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.CharField(max_length=200),
        ),
    ]