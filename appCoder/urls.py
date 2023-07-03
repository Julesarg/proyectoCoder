from django.urls import include, path
from appCoder import views

urlpatterns = [
    path('', views.inicio),
    path('cursos', views.inicio),
    path('profesores', views.profesores),
    path('estudiantes', views.estudiantes),
    path('entregables', views.entregables),
]