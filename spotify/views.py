from django.shortcuts import render


def entomos1(request):
    return render(request,'spotify/entomos-disidencia.html')
def entomos2(request):
    return render(request,'spotify/entomos-praxis.html')
def entomosep(request):
    return render(request,'spotify/entomos-ep.html')
def ermita1(request):
    return render(request,'spotify/ermita1.html')
def ermita2(request):
    return render(request,'spotify/ermita2.html')
def eternidad(request):
    return render(request,'spotify/eternidad.html')
def kreen(request):
    return render(request,'spotify/kreen.html')
def poncho(request):
    return render(request,'spotify/ponchoBriones.html')
def tiolo(request):
    return render(request,'spotify/tiolo.html')

