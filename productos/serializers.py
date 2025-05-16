from rest_framework import serializers
from .models import (
    Categoria, Talla, Marca, Color, Material, Estado, Publicacion
)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['cod_id', 'nombre']

class TallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talla
        fields = ['cod_id', 'nombre']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['cod_id', 'nombre']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['cod_id', 'nombre']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['cod_id', 'nombre']

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['cod_id', 'nombre']

class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = [
            'cod_id',
            'nombre',
            'descripcion',
            'categoria',
            'talla',
            'marca',
            'color',
            'material',
            'estado',
            'precio',
            'fecha_publicacion',
            'disponible',
            'imagen'
        ]