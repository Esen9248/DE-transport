from django import forms


class AddUserForm(forms.Form):
    name = forms.CharField(max_length=255)
    sur_name = forms.CharField(max_length=255)
    middle_name = forms.CharField(max_length=255)
    number = forms.IntegerField()
    info = forms.CharField(widget=forms.Textarea)

class LoginUser(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)