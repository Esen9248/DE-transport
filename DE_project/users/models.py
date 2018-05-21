from django.db import models
from django.urls import reverse
from django.conf import settings


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    email = models.EmailField()
    sur_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    number = models.IntegerField()
    info = models.TextField(null=True)
    auth_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('user-details', args=[self.slug])
