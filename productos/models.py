from django.db import models

class Categoria(models.Model):
    cod_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Talla(models.Model):
    cod_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    cod_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Color(models.Model):
    cod_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Material(models.Model):
    cod_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Estado(models.Model):
    cod_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Publicacion(models.Model):
    cod_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    talla = models.ForeignKey(Talla, on_delete=models.SET_NULL, null=True)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)

    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.precio} CLP"
