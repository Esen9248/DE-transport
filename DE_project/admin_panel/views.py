from django.shortcuts import render
from orders.models import Orders
def admin_job(request):
    orders = Orders.objects.all()
    return render(request, 'admin.html', locals())
