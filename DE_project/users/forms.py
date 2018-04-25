from django import forms
from .models import Users

class AddUserForm(forms.Form):
    name = forms.CharField(max_length=255)
    sur_name = forms.CharField(max_length=255)
    middle_name = forms.CharField(max_length=255)
    number = forms.IntegerField()
    info = forms.CharField(widget=forms.Textarea)
    def save(self):
        Users.objects.create(
            name=self.cleaned_data['name'],
            sur_name=self.cleaned_data['sur_name'],
            middle_name=self.cleaned_data['middle_name'],
            number=self.cleaned_data['number'],
            info=self.cleaned_data['info'],
        )

class LoginUser(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
