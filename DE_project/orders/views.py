from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Orders
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
@login_required

def orders(request):
    order = Orders.objects.all()
    return render(request, 'form_of_order.html', locals())
@login_required
def order_details(request, slug):
    order = get_object_or_404(Orders, slug = slug)
    return render(request, 'order_details.html', locals())  

@login_required
def post_order(request):
    page_name = 'Make An Order'
    form = OrderForm(request.POST or None, initial={'user': request.user.users})
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(reverse('cars:home'))
    return render(request, 'post_order.html', locals())    


@login_required
def post_edit(request, id):
    page_name = 'Edit Your Order'
    order = Orders.objects.get(id=id)
    form = OrderForm(request.POST or None, instance=order)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(reverse('cars:home'))
    return render(request, 'post_order.html', locals())   

@login_required
def delete_post(request, id):
    order = Orders.objects.get(id=id)
    
    if request.method == 'POST':
        order.delete()
        return redirect(reverse('cars:home'))

    return render(request, 'post_order.html', locals())         