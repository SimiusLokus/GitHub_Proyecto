from rest_framework import serializers
from .models import TipoUser, LlaveSeguridad, SuperUser, Admin, Supervisor

class TipoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUser
        fields = ['id', 'nombre']


class LlaveSeguridadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LlaveSeguridad
        fields = ['id', 'codigo']


class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperUser
        fields = ['iduser', 'tipouser', 'correo', 'usuario', 'contraseña', 'llave']


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['iduser', 'tipouser', 'correo', 'usuario', 'contraseña', 'llave']


class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = ['iduser', 'tipouser', 'correo', 'usuario', 'contraseña', 'llave']