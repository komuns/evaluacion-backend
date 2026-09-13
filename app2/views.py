from django.http import HttpResponse

def vista_tres(request):
    return HttpResponse("<h1>Hola desde la Vista 3 de App 2</h1>")

def vista_cuatro(request):
    return HttpResponse("<h1>Hola desde la Vista 4 de App 2</h1>")
  