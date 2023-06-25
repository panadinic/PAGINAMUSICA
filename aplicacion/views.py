from django.shortcuts import render, redirect, HttpResponse 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegistroForm
from django.views.generic import FormView
from .models import Cliente
from django.views.generic.base import TemplateView
import pdb
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class HomePageView(TemplateView):
    template_name = "aplicacion/index.html"
    
    
class ContactoPageView(TemplateView):
    template_name = "aplicacion/contacto.html"    
    
class ServiciosPageView(TemplateView):
    template_name = "aplicacion/servicios.html"   

class ClasesPageView(TemplateView):
    template_name = "aplicacion/clases.html"   

# class IniciarSesionPageView(TemplateView):
#     template_name = "aplicacion/iniciarSesion.html"
    
class IniciarSesionPageView(LoginView):
    template_name = 'aplicacion/iniciarSesion.html'
    
class CrearCuentaView(FormView):
    template_name = 'aplicacion/crearCuenta.html'
    form_class = RegistroForm


  


def enviar_mensaje(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        correo = request.POST['correo_electronico']
        servicio = request.POST['servicio']
        mensaje = request.POST['mensaje']
        total_carrito = request.GET.get('total_carrito')  # Obtener el valor con una cadena vacía como valor predeterminado
        servicios_seleccionados = request.GET.get('servicios_seleccionados')  # Obtener el valor con una cadena vacía como valor predeterminado

        # Validar si total_carrito es una cadena vacía y asignar None en su lugar
        total_carrito = int(total_carrito) if total_carrito else None

        cliente = Cliente(nombre=nombre, correo_electronico=correo, servicio=servicio, mensaje=mensaje, total_carrito=total_carrito, servicios_seleccionados=servicios_seleccionados)
        cliente.save()

        print("Datos guardados en la base de datos.")

        # Puedes realizar alguna acción adicional después de guardar los datos, como mostrar un mensaje de éxito o redireccionar a otra página.
        return render(request, 'aplicacion/index.html')
    else:
        return render(request, 'aplicacion/iniciarSesion.html')

    
    
def crear_cuenta(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        # pdb.set_trace() 
        if form.is_valid():
            mensaje = "entramos al valid"
            print(mensaje)                                
            form.save()
            # Realiza acciones adicionales después de guardar los datos
            return redirect('/iniciarSesion')
        else:
            mensaje = "esto no funciona"
            print(mensaje)
            # form = RegistroForm()
    else:
        form = RegistroForm()
    
    return render(request, 'aplicacion/crearCuenta.html', {'form': form})







# def login_view(request):
#     if request.method == 'POST':
#         correo = request.POST['correo']
#         contrasena = request.POST['contrasena']
#         user = authenticate(request, username=correo, password=contrasena)
#         if user is not None:
#             login(request, user)
#             mensaje = "login_efectivo"
#             print(mensaje)
#             # Inicio de sesión exitoso, redirigir a la página de inicio
#             return redirect('home')
#         else:
#             # Credenciales incorrectas, mostrar mensaje de error
#             error_message = 'Credenciales incorrectas. Inténtalo nuevamente.'
#             mensaje2 ="no funciona"
#             print(mensaje2)
            
#             return render(request, 'iniciarSesion.html', {'error_message': error_message})
#     else:
#         return render(request, 'iniciarSesion.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['contrasena']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Inicio de sesión exitoso, redirigir a la página de inicio
            return redirect('home')
        else:
            # Credenciales incorrectas, mostrar mensaje de error
            error_message = 'Credenciales incorrectas. Inténtalo nuevamente.'
            return render(request, 'iniciarSesion.html', {'error_message': error_message})
    else:
        return render(request, 'iniciarSesion.html')

def logout_view(request):
    logout(request)
    # Redirige a la página de inicio o a cualquier otra página que desees
    return redirect('home')    