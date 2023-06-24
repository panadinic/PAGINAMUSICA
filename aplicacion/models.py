from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone



# Create your models here.

# class Cliente(models.Model):
#     nombre = models.CharField(max_length=100)
#     correo_electronico = models.EmailField()
#     SERVICIOS_CHOICES = [
#         ('servicio1', 'Mezcla'),
#         ('servicio2', 'Mezcla_Master'),
#         ('servicio3', 'Master'),
#         ('servicio4', 'Mezcla_Master_Edicion'),
#         ('servicio5', 'Grabacion'),
#         ('servicio6', 'Produccion_Completa'),
#         ('servicio7', 'clases'),
#     ]
#     servicio = models.CharField(max_length=20, choices=SERVICIOS_CHOICES, null=True)
#     mensaje = models.TextField()

#     def __str__(self):
#         return self.nombre
 
 
 
 
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
    total_carrito = models.IntegerField(null=True)
    servicios_seleccionados = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombre
    


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('El campo email debe estar configurado')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    nombre = models.CharField(max_length=255, null=False, blank=False)
    telefono = models.CharField(max_length=12, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    fechaNacimiento = models.DateField(null=False, blank=False, default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombre']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
