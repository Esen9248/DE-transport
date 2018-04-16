from django.contrib import admin
from .models import Users
# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Users, UsersAdmin)
