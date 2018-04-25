from django.contrib import admin
from .models import Orders

class OrderAdmin(admin.ModelAdmin):
    prepoluted_fields = {"slug": ("cars",)}


admin.site.register(Orders, OrderAdmin)    
# Register your models here.
