from rest_framework import serializers
from .models import PerfilUsuario

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = ['id', 'nombre', 'apellido', 'correo', 'telefono', 'fecha_registro', 'activo']