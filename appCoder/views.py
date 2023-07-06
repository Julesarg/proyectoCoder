from django.http import HttpResponse
from django.shortcuts import render
from appCoder.forms import CursoFormulario
from appCoder.models import Curso

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

def cursoFormulario(request):
    if request.method == 'POST':
        myForm = CursoFormulario(request.POST)
        print(myForm)
        if myForm.is_valid():
            informacion = myForm.cleaned_data
            curso = Curso( nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()
            return render(request, 'inicio.html')
    else:
        myForm = CursoFormulario()
    return render(request, 'cursoFormulario.html', {'myForm': myForm})