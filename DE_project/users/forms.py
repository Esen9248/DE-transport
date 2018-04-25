from django import forms
from .models import Users
from django.contrib.auth.models import User as DjangoUser
from django.utils.text import slugify

class AddUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=255)
    sur_name = forms.CharField(max_length=255)
    middle_name = forms.CharField(max_length=255)
    number = forms.IntegerField()
    info = forms.CharField(widget=forms.Textarea, required=False)
    def save(self):
        django_user = DjangoUser.objects.create(
            username=self.cleaned_data['username'],
            first_name=self.cleaned_data['name'],
            last_name=self.cleaned_data['sur_name']
        )
        django_user.set_password(self.cleaned_data['password'])
        django_user.save()
        slug = slugify(self.cleaned_data['name'])
        Users.objects.create(
            auth_user = django_user,
            name=self.cleaned_data['name'],
            sur_name=self.cleaned_data['sur_name'],
            middle_name=self.cleaned_data['middle_name'],
            number=self.cleaned_data['number'],
            info=self.cleaned_data['info'],
            slug=slug
        )
    

class LoginUser(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
