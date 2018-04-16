from django.contrib import admin
from .models import Orders

@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    pass
# Register your models here.
