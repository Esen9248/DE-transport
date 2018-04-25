from django.db import models
from django.db.models import permalink
from users.models import Users
from django.urls import reverse


class Orders(models.Model):
    place = models.CharField(max_length=200)
    time_at = models.DateTimeField()
    time_for_order = models.DateField()
    cars = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    car_quantity = models.IntegerField()
    car_roominess = models.IntegerField()
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.cars
        
    def get_absolute_url(self):
        return reverse('order-details', args=[self.slug])

