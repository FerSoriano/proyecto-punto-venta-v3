from django.shortcuts import render, redirect
from django.http import HttpResponse
# from functools import wraps # pendiente cuando se implemente loggin


# Create your views here.
def home(request):
    return HttpResponse('Hello world')


def login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')

        # imprimimos valores de prueba
        print(user, password)

        # Redireccionar para evitar reenviar el formulario al refrescar
        return redirect('home')

    # Si es GET, muestra todos los posts
    return render(
        request,
        'usuarios/login.html'
    )


def dashboard_admin(request):
    return render(
        request,
        'usuarios/admin.html'
    )


def dashboard_ventas(request):
    return render(
        request,
        'usuarios/vendedor.html'
    )
