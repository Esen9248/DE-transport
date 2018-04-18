from django.db import models
from users.models import Users
from django.urls import reverse


class Orders(models.Model):
    place = models.CharField(max_length=200, unique=True)
    time_at = models.DateField()
    time_for_order = models.DateField()
    cars = models.CharField(max_length=100)
    car_quantity = models.IntegerField()
    car_roominess = models.IntegerField()
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('order-details', args=[self.slug])

    def __str__(self):
        return f'{self.place}, {self.user}'
