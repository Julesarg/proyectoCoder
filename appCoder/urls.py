from django.urls import path
from appCoder import views
urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('inicio', views.inicio, name="inicio"),
    path('cursos', views.cursos, name="cursos"),
    path('profesores', views.profesores, name="profesores"),
    path('estudiantes', views.estudiantes, name="estudiantes"),
    path('entregables', views.entregables, name="entregables"),
]