from django.shortcuts import render, redirect
from django.http import HttpResponse
from inventario.services import contar_productos_activos
# from functools import wraps # pendiente cuando se implemente loggin


# Create your views here.
def home(request):
    # TODO: completar funcion de Home
    # si no esta loggeado, redireccinar al loggin
    # si esta loggeado, mandar a su dashboard (vendedor o admin)
    return redirect('login')


def login(request):
    # TODO: Pendiente completar Login
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password') # noqa

        # redireccionamiento de prueba
        if user == 'admin':
            return redirect('dashboard_admin')
        if user == 'vend':
            return redirect('dashboard_ventas')

    return render(
        request,
        'usuarios/login.html'
    )


def dashboard_admin(request):
    productos_activos = contar_productos_activos()
    return render(
        request,
        'usuarios/dashboard_admin.html',
        {
            'productos_activos': productos_activos
        }
    )


def dashboard_ventas(request):
    return render(
        request,
        'usuarios/dashboard_vendedor.html'
    )
