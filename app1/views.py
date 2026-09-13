from django.http import HttpResponse

def vista_uno(request):
    return HttpResponse("<h1>Hola desde la Vista 1 de App 1</h1>")

def vista_dos(request):
    return HttpResponse("<h1>Hola desde la Vista 2 de App 1</h1>")