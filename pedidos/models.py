from django.db import models
from usuarios.models import PerfilUsuario
from pagos.models import Pago
from productos.models import Publicacion

class EstadoPedido(models.Model):
    nombre = models.CharField(max_length=30)  # Ej: Pendiente, Enviado, Cancelado, Entregado

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.ForeignKey(EstadoPedido, on_delete=models.SET_NULL, null=True)
    pago = models.ForeignKey(Pago, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario} - {self.estado}"


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detalles', on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.publicacion} x{self.cantidad} (Pedido #{self.pedido.id})"
