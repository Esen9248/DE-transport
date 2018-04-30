from django import forms
from django.forms import ModelForm
from .models import Orders

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = [
            'place',
            'time_at',
            'time_from',
            'time_to',
            'cars',
            'car_quantity',
            'number_of_passenger_seat',
            'user'
        ]
        widgets = {
            'user': forms.HiddenInput(),
            'time_at': forms.DateInput(attrs={'class':'datepicker'}),
            'time_from': forms.DateInput(attrs={'id': 'from'}),
            'time_to': forms.DateInput(attrs={'id': 'to'})
        }
