#Funciones que ejecutan la logica
from django.http import response
from django.http import HttpResponse

def saludo(request):
    return HttpResponse('Hola mundo')

def despedida(request):
    return HttpResponse('Hasta luego')

def adulto(request, edad, nombre):
    if edad >= 18:
        return HttpResponse(f'Hola {nombre} eres adulto :)')
    else: return HttpResponse(f'Hola {nombre}, eres menor de edad :(')