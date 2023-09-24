# Generated by Django 4.0.4 on 2023-08-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='booked_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
