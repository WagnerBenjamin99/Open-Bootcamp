import email
from django.shortcuts import render
from django.http import HttpResponse
from .models import autor, entrada

def queris(request):
    autores=autor.objects.all()

    
    filtrado=autor.objects.filter(email='reginameyers@example.net')
    return render(request, 'post/queris.html', {'autores':autores, 'filtrado':filtrado})