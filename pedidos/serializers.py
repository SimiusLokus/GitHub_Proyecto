from rest_framework import serializers
from .models import EstadoPedido, Pedido, DetallePedido
from productos.models import Publicacion

class EstadoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPedido
        fields = ['id', 'nombre']


class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = ['id', 'pedido', 'publicacion', 'cantidad', 'precio_unitario']


class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'fecha_pedido', 'estado', 'pago', 'total', 'detalles']