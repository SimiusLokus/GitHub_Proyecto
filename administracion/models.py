import random
import string
from django.db import models

class TipoUser(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class LlaveSeguridad(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=8, unique=True, editable=False)

    def generar_codigo(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def save(self, *args, **kwargs):
        if not self.codigo:
            nuevo_codigo = self.generar_codigo()
            while LlaveSeguridad.objects.filter(codigo=nuevo_codigo).exists():
                nuevo_codigo = self.generar_codigo()
            self.codigo = nuevo_codigo
        super().save(*args, **kwargs)

    def __str__(self):
        return self.codigo


# Base común para los tres tipos
class BaseCuenta(models.Model):
    iduser = models.AutoField(primary_key=True)
    tipouser = models.ForeignKey(TipoUser, on_delete=models.CASCADE)
    correo = models.EmailField(unique=True)
    usuario = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=128)
    llave = models.ForeignKey(LlaveSeguridad, on_delete=models.PROTECT)

    class Meta:
        abstract = True  # Evita que Django cree una tabla para esta clase base

    def __str__(self):
        return f"{self.usuario} ({self.tipouser})"


class SuperUser(BaseCuenta):
    pass

class Admin(BaseCuenta):
    pass

class Supervisor(BaseCuenta):
    pass

