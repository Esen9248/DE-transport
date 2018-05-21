from django.db import models
from django.db.models import permalink
from users.models import Users
from cars.models import Cars
from django.urls import reverse
from django.utils.text import slugify
from django.db.models import signals
from .tasks import order_verified_send_mail

class Orders(models.Model):
    place = models.CharField(max_length=200)
    time_at = models.DateTimeField()
    time_from = models.DateTimeField()
    time_to = models.DateTimeField()
    cars = models.ManyToManyField(Cars)
    slug = models.SlugField(max_length=100, unique=True)
    car_quantity = models.IntegerField()
    info_about_order = models.TextField()
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
        
def user_order_save(sender, instance, signal, *args, **kwargs):
    email = instance.user.email
    order_verified_send_mail.delay(email, 'Your order is verified')

signals.post_save.connect(user_order_save, sender=Orders)

