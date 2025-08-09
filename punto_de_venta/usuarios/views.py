from django.shortcuts import render, redirect
from django.http import HttpResponse
# from functools import wraps # pendiente cuando se implemente loggin


# Create your views here.
def home(request):
    # TODO: completar funcion de Home
    # si no esta loggeado, redireccinar al loggin
    # si esta loggeado, mandar a su dashboard (vendedor o admin)
    return HttpResponse('Hello world')


def login(request):
    # TODO: Pendiente completar Login
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')

        # imprimimos valores de prueba
        print(user, password)

        # Redireccionar para evitar reenviar el formulario al refrescar
        return redirect('home')

    return render(
        request,
        'usuarios/login.html'
    )


def dashboard_admin(request):
    return render(
        request,
        'usuarios/dashboard_admin.html'
    )


def dashboard_ventas(request):
    return render(
        request,
        'usuarios/dashboard_vendedor.html'
    )
