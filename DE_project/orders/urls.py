from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='order'),
    path('<str:slug>/', views.order_details, name='order_details')
]
