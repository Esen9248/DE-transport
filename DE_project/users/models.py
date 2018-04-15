from django.db import models
from django.urls import reverse
# Create your models here.
class Users_number(models.Model):
    number = models.IntegerField()
    def __str__(self):
        return f'{self.number}'


class Users(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    sur_name = models.CharField(max_length=300)
    middle_name = models.CharField(max_length=300)
    number = models.ForeignKey(Users_number, on_delete=models.CASCADE)
    info = models.TextField()
    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse('user-details', args=[self.slug])