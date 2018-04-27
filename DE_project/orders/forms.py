from django import forms
from django.forms import ModelForm
from .models import Orders

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = [
            'place',
            'time_at',
            'time_for_order',
            'cars',
            'car_quantity',
            'car_roominess',
            'user'
        ]
        widgets = {
            'user': forms.HiddenInput(),
            'time_at': forms.DateInput(attrs={'class':'datepicker'}),
        }
