from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_view, name='users'),
    path('<str:slug>/', views.user_details, name='user-details')
]
