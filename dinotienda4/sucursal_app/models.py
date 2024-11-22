from django.db import models

# Create your models here.
class Sucursal(models.Model):
    id_suc=models.CharField(primary_key=True,max_length=6)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    horario=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    CP=models.CharField(max_length=20)
    web=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre