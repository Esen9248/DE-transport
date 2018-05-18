"""DE_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include,path
from orders import urls as orders_urls
from users import urls as users_urls
from users import views as users_views
from cars import views as cars_views
from admin_panel import views

urlpatterns = [
    path('', users_views.login_user, name='login-user'),
    path('logout', users_views.logout_user, name='logout-user'),
    path('register-user', users_views.register_user, name='register-user'),
    path('admin_panel/', include('admin_panel.urls')),
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),
    path('home/', include('cars.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
