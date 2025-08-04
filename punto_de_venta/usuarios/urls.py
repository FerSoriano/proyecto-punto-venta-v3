
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('inicio/admin', views.dashboard_admin, name='dashboard_admin'),
    path('inicio/ventas', views.dashboard_ventas, name='dashboard_ventas'),
]
