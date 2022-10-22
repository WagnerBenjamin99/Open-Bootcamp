from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def proyectos(request):
    return render(request, 'proyectos.html', {})