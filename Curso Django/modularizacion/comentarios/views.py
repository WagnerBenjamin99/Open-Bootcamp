import email
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import comment, user


def test(request):
    return HttpResponse('Hola mundo')

# def create(request):
#     # comentario=comment(name='Benjamin', comment='Este es un comentario')
#     # comentario.save()
#     comentario=comment.objects.create(name='Miriam')
#     return HttpResponse('Ruta para probar la creacion de modelos')

def delete(request):

#     # comentario = comment.objects.get(id=1)
#     # comentario.delete()
#     comment.objects.filter(id=2).delete()
    user.objects.filter(id=2).delete()
    return HttpResponse('Buscando y borrando objetos')

def create(request):
    usuario = user.objects.create(nombre='Benjamin', apellido='Wagner', email='benja')
    return HttpResponse('Ruta para probar la creacion de modelos')