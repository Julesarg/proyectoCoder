from django.http import HttpResponse
from django.shortcuts import render
from appCoder.models import Curso
from django.template import loader

# Create your views here.

def curso(self):
    curso = Curso(nombre='Desarrollo web', camada= '55865')
    curso.save()

    documento = f'Curso: {curso.nombre} Camada:{curso.camada}'

    return HttpResponse(documento)

def inicio(request):
    return render(request, 'inicio.html')

def cursos(request):
    return render(request, 'cursos.html')

def profesores(request):
    return render(request, 'profesores.html')

def estudiantes(request):
    return render(request, 'estudiantes.html')

def entregables(request):
    return render(request, 'entregables.html')