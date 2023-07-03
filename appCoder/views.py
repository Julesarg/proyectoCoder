from django.http import HttpResponse
from django.shortcuts import render
from appCoder.models import Curso

# Create your views here.

def curso(self):
    curso = Curso(nombre='Desarrollo web', camada= '55865')
    curso.save()

    documento = f'Curso: {curso.nombre} Camada:{curso.camada}'

    return HttpResponse(documento)

def inicio(request):
    return HttpResponse('vista inicio')

def cursos(request):
    return HttpResponse('vista cursos')

def profesores(request):
    return HttpResponse('vista profesores')

def estudiantes(request):
    return HttpResponse('vista estudiantes')

def entregables(request):
    return HttpResponse('vista entregables')