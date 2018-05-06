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
            'info_about_order',
            'number_of_passenger_seat',
            'user'
        ]
        widgets = {
            'user': forms.HiddenInput(),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'time_at': forms.DateInput(attrs={'class':'datepicker form-control'}),
            'time_from': forms.DateInput(attrs={'id': 'from', 'class': 'form-control'}),
            'time_to': forms.DateInput(attrs={'id': 'to', 'class': 'form-control'}),
            'cars': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'info_about_order': forms.TextInput(attrs={'class': 'form-control', 'rows': '3'}),
        
        }
