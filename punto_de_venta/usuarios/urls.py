
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='root'),
    path('login', views.login, name='login'),
    path('usuarios/admin/dashboard', views.dashboard_admin, name='dashboard_admin'),
    path('usuarios/ventas/dashboard', views.dashboard_ventas, name='dashboard_ventas'),
]
