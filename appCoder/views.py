from django.http import HttpResponse
from django.shortcuts import render
from appCoder.models import Curso

# Create your views here.

def curso(self):
    curso = Curso(nombre='Desarrollo web', camada= '55865')
    curso.save()

    documento = f'Curso: {curso.nombre} Camada:{curso.camada}'

    return HttpResponse(documento)