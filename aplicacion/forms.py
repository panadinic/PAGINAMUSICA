from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistroForm(UserCreationForm):
    fechaNacimiento = forms.DateField(label="Fecha de Nacimiento")
    email = forms.EmailField(label="Correo Electrónico")
    telefono = forms.CharField(label="Teléfono")
    nombre = forms.CharField(label="Nombre")

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('fechaNacimiento', 'email', 'telefono', 'nombre')