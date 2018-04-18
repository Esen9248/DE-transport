from django.db import models
from users.models import Users

class Orders(models.Model):
    place = models.CharField(max_length=200)
    time_at = models.IntegerField()
    time_for_order = models.IntegerField()
    cars = models.CharField(max_length=100)
    car_quantity = models.IntegerField()
    car_roominess = models.IntegerField()
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.place}, {self.user}'