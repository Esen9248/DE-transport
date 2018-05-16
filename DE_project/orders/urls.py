from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('post-order/', views.post_order, name='post-order'),
    path('edit/<str:id>/', views.post_edit, name='post-edit'),
    path('delete/<str:id>/', views.delete_post, name='delete-post'),
    path('<str:slug>/', views.order_details, name='order-details')
]
