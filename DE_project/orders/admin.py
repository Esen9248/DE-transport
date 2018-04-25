from django.contrib import admin
from .models import Orders

class OrderAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("place",)}


admin.site.register(Orders, OrderAdmin)    
# Register your models here.
