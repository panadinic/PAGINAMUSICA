from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistroForm(UserCreationForm):
    # Agrega los campos adicionales que deseas para el registro de usuarios
    fecha_nacimiento = forms.DateField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('fecha_nacimiento',)
