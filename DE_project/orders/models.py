from django.db import models
from django.db.models import permalink
from users.models import Users
from django.urls import reverse
from django.utils.text import slugify


class Orders(models.Model):
    place = models.CharField(max_length=200)
    time_at = models.DateTimeField()
    time_from = models.DateTimeField()
    time_to = models.DateTimeField()
    cars = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    car_quantity = models.IntegerField()
    number_of_passenger_seat = models.IntegerField()
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.place

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.place)
        return super(Orders, self).save(*args, **kwargs)    

        
    def get_absolute_url(self):
        return reverse('order-details', args=[self.slug])

