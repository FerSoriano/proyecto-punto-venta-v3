from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    existencias = models.IntegerField()
    nivel_reorden = models.IntegerField()
    status = models.BooleanField(default=True)
    fecha_alta = models.DateTimeField(auto_now=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    @property  # se calcula dinamicamente en lugar de guardarse en la BBDD
    def resurtir(self):
        return self.nivel_reorden >= self.existencias

    def __str__(self):
        return f"{self.nombre} - Estatus: {self.status} - Resurtir {self.resurtir}"
