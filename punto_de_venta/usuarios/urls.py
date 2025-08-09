
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('admin/dashboard', views.dashboard_admin, name='dashboard_admin'),
    path('ventas/dashboard', views.dashboard_ventas, name='dashboard_ventas'),
]
