from django.db import models
from django.urls import reverse
# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    sur_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    number = models.IntegerField()
    info = models.TextField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('user-details', args=[self.slug])