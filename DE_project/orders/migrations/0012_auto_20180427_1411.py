# Generated by Django 2.0.4 on 2018-04-27 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20180427_1351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='car_roominess',
            new_name='number_of_passenger_seat',
        ),
    ]
