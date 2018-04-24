from django.shortcuts import render, get_object_or_404
from .models import Orders
from django.contrib.auth.decorators import login_required
@login_required
def orders(request):
    order = Orders.objects.all()
    return render(request, 'form_of_order.html', locals())
@login_required
def order_details(request, slug):
    orders = get_object_or_404(Orders, slug = slug)
    return render(request, 'form_details.html', locals())    