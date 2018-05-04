from django.contrib import admin
from .models import Cars

class CarsAdmin(admin.ModelAdmin):
     prepopulated_fields = {"slug": ("brand", "model",)}
 
admin.site.register(Cars, CarsAdmin)    

