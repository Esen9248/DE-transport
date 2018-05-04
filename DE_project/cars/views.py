from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Cars
from django.contrib.auth.decorators import login_required


# Create your views here.@login_required
@login_required
def home(request):
    cars = Cars.objects.all()
    return render(request, 'home.html', locals())

    
@login_required
def car_details(request, slug):
    cars = get_object_or_404(Cars, slug=slug)
    return render(request, 'car_details.html', locals())    
