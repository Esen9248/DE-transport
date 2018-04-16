from django.shortcuts import render
from .models import Orders

def orders(request):
    order = Orders.objects.all()
    return render(request, 'form_of_order.html', locals())