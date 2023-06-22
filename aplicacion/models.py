from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    SERVICIOS_CHOICES = [
        ('servicio1', 'Mezcla'),
        ('servicio2', 'Mezcla_Master'),
        ('servicio3', 'Master'),
        ('servicio4', 'Mezcla_Master_Edicion'),
        ('servicio5', 'Grabacion'),
        ('servicio6', 'Produccion_Completa'),
        ('servicio7', 'clases'),
    ]
    servicio = models.CharField(max_length=20, choices=SERVICIOS_CHOICES, null=True)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
    


class CustomUser(AbstractUser):
    telefono = models.CharField(max_length=12)
    fechaNacimiento = models.DateField(null=True, default=None)


    # Agrega otros campos adicionales según tus necesidades

    def __str__(self):
        return self.username




