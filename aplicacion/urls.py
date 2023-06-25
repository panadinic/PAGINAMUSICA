
from django.urls import path
from .views import HomePageView, ContactoPageView, ServiciosPageView, ClasesPageView, IniciarSesionPageView, CrearCuentaView, enviar_mensaje, crear_cuenta, login_view, logout_view
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',HomePageView.as_view(), name="home" ),
    path('contacto/',ContactoPageView.as_view(), name="contacto" ),
    path('servicios/',ServiciosPageView.as_view(), name="servicios" ),
    path('clases/',ClasesPageView.as_view(), name="clases" ),
    # path('iniciarSesion/',IniciarSesionPageView.as_view(), name="iniciarSesion" ),
    path('iniciarSesion/', LoginView.as_view(template_name='aplicacion/iniciarSesion.html'), name="iniciarSesion"),
    path('enviar_mensaje/',enviar_mensaje,name="enviar_mensaje"),
    path('crearCuenta/', CrearCuentaView.as_view(), name="crearCuenta"),
    path('crearCuenta/submit/', crear_cuenta, name="crearCuentaSubmit"),
    path('contacto/<int:total_carrito>/<str:servicios>/', ContactoPageView.as_view(), name="contacto_parametros"),
    path('iniciar_sesion' ,login_view, name="iniciar_sesion"),
    path('logout/', logout_view, name='logout'),
    
    
    
    
]
