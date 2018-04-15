from django.shortcuts import render, get_object_or_404
from .models import Users
# Create your views here.
def users_view(request):
    users = Users.objects.all()
    return render(request, 'users/users.html', locals())

def user_details(request, slug):
    user = get_object_or_404(Users, slug=slug)
    return render(request, 'users/details.html', locals())