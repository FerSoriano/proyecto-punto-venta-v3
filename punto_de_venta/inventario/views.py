from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from .models import Producto


def lista_productos(request):
    productos = Producto.objects.all().order_by('nombre')
    return render(
        request,
        'inventario/productos.html',
        {
            'productos': productos
        }
    )


def crear_producto(request):
    pass


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.precio_compra = request.POST.get('precio_compra')
        producto.precio_venta = request.POST.get('precio_venta')
        producto.existencias = request.POST.get('existencias')
        producto.nivel_reorden = request.POST.get('nivel_reorden')

        producto.save()
        return redirect('lista_productos')

    return render(
        request,
        'inventario/editar_producto.html',
        {
            'producto': producto
        }
    )


def eliminar_producto(request):
    pass
