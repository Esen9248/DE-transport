from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cars'
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:slug>/', views.car_details, name='car-details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)