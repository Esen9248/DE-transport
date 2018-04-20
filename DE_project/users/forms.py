from django import forms
from models import *

class AddUserForm(forms.Form):
    name = forms.CharField(max_length=255)
    sur_name = forms.CharField(max_length=255)
    middle_name = forms.CharField(max_length=255)
    number = forms.IntegerField()
