from django.contrib import admin
from .models import Orders

class OrderAdmin(admin.ModelAdmin):
    exclude = ['place']
    prepoluted_fields = {'slug': ('cars',)}


admin.site.register(Orders)    
# Register your models here.
