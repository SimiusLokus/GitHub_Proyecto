from rest_framework import serializers
from .models import MetodoPago, Pago

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = ['id', 'nombre']


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = [
            'id',
            'monto',
            'fecha_pago',
            'estado',
            'metodo',
            'transaccion_externa',
            'observacion'
        ]