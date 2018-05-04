from django.db import models
from django.urls import reverse

class Cars(models.Model):
    brand = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=100, unique=True)
    year = models.IntegerField()
    volume = models.IntegerField()
    color = models.CharField(max_length=100)
    image = models.FileField(upload_to='image', blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return u'%s %s' % (self.brand, self.model)
     
    # def get_absolute_url(self):
    #     return reverse('car-details', args=[self.slug])


