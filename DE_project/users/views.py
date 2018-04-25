from django.shortcuts import render, get_object_or_404, redirect
from .models import Users
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def users_view(request):
    users = Users.objects.all()
    return render(request, 'users/users.html', locals())
@login_required
def user_details(request, slug):
    user = get_object_or_404(Users, slug=slug)
    return render(request, 'users/details.html', locals())

def login_user(request):
    next_url = request.GET.get('next', reverse('home'))
    login_user_form = LoginUser(request.POST or None)
    if login_user_form.is_valid():
        username = login_user_form.cleaned_data['username']
        password = login_user_form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_url)
        else:
            error_message = 'Can`t login' 
    return render(request, 'users/loginuser.html', locals())
@login_required
def logout_user(request):
    logout(request)
    return redirect(reverse('login-user'))

@login_required
def home(request):
    return render(request, 'home.html', locals())