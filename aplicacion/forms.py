from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from aplicacion.models import CustomUser




class RegistroForm(UserCreationForm):
    nombre = forms.CharField(label='Nombre Completo')
    username = forms.CharField(label='Nombre de usuario')
    telefono = forms.CharField(label="Teléfono")
    email = forms.EmailField(label='Correo')
    fechaNacimiento = forms.DateField(label="Fecha de Nacimiento")
    password1  = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2  = forms.CharField(label='Re Contraseña', widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].label = 'Nombre Completo'
        self.fields['nombre'].help_text = 'Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Re Contraseña'
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ( 'nombre','username', 'telefono', 'email', 'fechaNacimiento', 'password1', 'password2')

