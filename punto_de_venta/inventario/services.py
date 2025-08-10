from .models import Producto


def contar_productos_activos() -> int:
    total_productos = 0
    productos = Producto.objects.filter(status=True)
    for producto in productos:
        total_productos += producto.existencias
    return total_productos
