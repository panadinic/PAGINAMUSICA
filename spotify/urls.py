from django.urls import path
from .views import entomos1,entomos2,entomosep,ermita1,ermita2,eternidad,kreen,poncho,tiolo

urlpatterns = [
    
path('spotify/entomos-disidencia/', entomos1, name='entomos1'),
path('spotify/entomos-praxis/', entomos2, name='entomos2'),
path('spotify/entomos-ep/', entomosep, name='entomosep'),
path('spotify/ermita1/', ermita1, name='ermita1'),
path('spotify/ermita2/', ermita2, name='ermita2'),
path('spotify/eternidad/', eternidad, name='eternidad'),
path('spotify/kreen/', kreen, name='kreen'),
path('spotify/ponchoBriones/', poncho, name='poncho'),
path('spotify/tiolo/', tiolo, name='tiolo'),         
    
    
    
]