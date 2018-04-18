from django.db import models
from users.models import Users
from django.urls import reverse


class Orders(models.Model):
    place = models.CharField(max_length=200, unique=True)
    time_at = models.IntegerField()
    time_for_order = models.IntegerField()
    cars = models.CharField(max_length=100)
    car_quantity = models.IntegerField()
    car_roominess = models.IntegerField()
    User = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.place

    def get_absolute_url(self):
        return reverse('order_details', args=[self.slug])

    def __str__(self):
        return '{} {} {} {} {} {}'.format(
            self.palace, 
            self.time_at, self.time_for_order,
            self.cars, self.car_quantity, self.car_roominess  
          )
