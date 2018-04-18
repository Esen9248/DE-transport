from django.shortcuts import render, get_object_or_404
from .models import Orders

def orders(request):
    order = Orders.objects.all()
    return render(request, 'form_of_order.html', locals())

def order_details(request, slug):
    cars = get_object_or_404(Orders, slug = slug)
    return render(request, 'form_details.html', locals())    