from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegistroForm
from django.views.generic import FormView


from .models import Cliente
from django.views.generic.base import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = "aplicacion/index.html"
    
    
class ContactoPageView(TemplateView):
    template_name = "aplicacion/contacto.html"    
    
class ServiciosPageView(TemplateView):
    template_name = "aplicacion/servicios.html"   

class ClasesPageView(TemplateView):
    template_name = "aplicacion/clases.html"   

class IniciarSesionPageView(TemplateView):
    template_name = "aplicacion/iniciarSesion.html"
    
# class CrearCuentaPageView(TemplateView):
#     template_name = 'aplicacion/crearCuenta.html'
    
class CrearCuentaView(FormView):
    template_name = 'aplicacion/crearCuenta.html'
    form_class = RegistroForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, '¡Cuenta creada exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear la cuenta. Por favor, revise los datos ingresados.')
        return super().form_invalid(form)    
       

def enviar_mensaje(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        correo = request.POST['correo_electronico']
        servicio = request.POST['servicio']
        mensaje = request.POST['mensaje']

      
        cliente = Cliente(nombre=nombre, correo_electronico=correo, servicio=servicio, mensaje=mensaje)
        cliente.save()

        print("Datos guardados en la base de datos.")

        # Puedes realizar alguna acción adicional después de guardar los datos, como mostrar un mensaje de éxito o redireccionar a otra página.
        return render(request, 'aplicacion/index.html')
    else:
        return render(request, 'aplicacion/iniciarSesion.html')
    
    




