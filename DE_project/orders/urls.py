from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='order'),
    path('post-order/', views.post_order, name='post-order'),
    path('<str:slug>/', views.order_details, name='order-details')
]
