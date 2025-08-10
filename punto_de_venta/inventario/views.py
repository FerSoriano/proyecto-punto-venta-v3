from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponseNotFound
from django.contrib import messages

from .models import Producto


def lista_productos(request):
    productos = Producto.objects.order_by('nombre')
    return render(
        request,
        'inventario/productos.html',
        {
            'productos': productos
        }
    )


def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio_compra = request.POST.get('precio_compra')
        precio_venta = request.POST.get('precio_venta')
        existencias = request.POST.get('existencias')
        nivel_reorden = request.POST.get('nivel_reorden')

        try:
            precio_compra = float(precio_compra)
            precio_venta = float(precio_venta)
            existencias = int(existencias)
            nivel_reorden = int(nivel_reorden)
        except ValueError:
            messages.error(request, "Los campos numéricos deben contener valores válidos.")
            return render(request, 'inventario/crear_producto.html')

        producto = Producto.objects.filter(nombre__iexact=nombre).first()  # omite mayusculas y minusculas

        if producto:
            messages.error(request, f'El producto "{nombre}" ya existe. Intenta de nuevo.')
            return render(request, 'inventario/crear_producto.html')

        if precio_compra >= precio_venta:
            messages.error(request, "El Precio de Compra no puede ser mayor o igual que el Precio de Venta.")
            return render(request, 'inventario/crear_producto.html')

        if existencias < nivel_reorden:
            messages.error(request, "Las Existencias no pueden ser menores que el Nivel de Reorden.")
            return render(request, 'inventario/crear_producto.html')

        Producto.objects.create(
            nombre=nombre,
            precio_compra=precio_compra,
            precio_venta=precio_venta,
            existencias=existencias,
            nivel_reorden=nivel_reorden
        )

        messages.success(request, f'El producto {nombre} se creo exitosamente.')
        return redirect('lista_productos')

    return render(request, 'inventario/crear_producto.html')


def reactivar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.status = True
        producto.save()
        messages.success(request, f'El producto "{producto.nombre}" se dio de alta nuevamente.')
        return redirect('lista_productos')
    return redirect('lista_productos')


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.precio_compra = request.POST.get('precio_compra')
        producto.precio_venta = request.POST.get('precio_venta')
        producto.existencias = request.POST.get('existencias')
        producto.nivel_reorden = request.POST.get('nivel_reorden')

        producto.save()
        messages.info(request, f'El producto "{producto.nombre}" ha sido modificado exitosamente.')
        return redirect('lista_productos')

    return render(
        request,
        'inventario/editar_producto.html',
        {
            'producto': producto
        }
    )


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.status = False
        producto.save()
        messages.success(request, f'El producto "{producto.nombre}" ha sido eliminado exitosamente.')
        return redirect('lista_productos')
    return redirect('lista_productos')
