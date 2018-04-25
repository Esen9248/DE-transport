from django import forms
from .models import Orders

class OrderForm(forms.Form):
    place = forms.CharField(max_length=200)
    time_at = forms.DateTimeField()
    time_for_order = forms.DateField()
    and_of_time = forms.DateField()
    cars = forms.CharField(max_length=100)
    car_quantity = forms.IntegerField()
    car_roominess = forms.IntegerField()