
from django.urls import path
from .views import HomePageView, ContactoPageView, ServiciosPageView, ClasesPageView, IniciarSesionPageView, CrearCuentaView, enviar_mensaje,crear_cuenta


urlpatterns = [
    path('',HomePageView.as_view(), name="home" ),
    path('contacto/',ContactoPageView.as_view(), name="contacto" ),
    path('servicios/',ServiciosPageView.as_view(), name="servicios" ),
    path('clases/',ClasesPageView.as_view(), name="clases" ),
    path('iniciarSesion/',IniciarSesionPageView.as_view(), name="iniciarSesion" ),
    path('crearCuenta/', CrearCuentaView.as_view(), name="crearCuenta"),
    path('enviar_mensaje/',enviar_mensaje,name="enviar_mensaje"),
    ## path de spotify
     path('crearCuenta/submit/', crear_cuenta, name="crearCuentaSubmit"),
    
    
    
    
]
