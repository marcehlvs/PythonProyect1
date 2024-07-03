from django.urls import path, include
from entidades.views import *
urlpatterns = [
    path('', home, name='home'),

    #cursos

    path('cursos/', cursos, name='cursos'),
    path('cursoForm/', cursoForm, name='cursoForm'),
    path('cursoUpdate/<id_curso>/', cursoUpdate, name='cursoUpdate'),
    path('cursoDelete/<id_curso>/', cursoDelete, name='cursoDelete'),

    #profesores

    path('profesores/', profesores, name='profesores'),
    path('profesorForm/', profesorForm, name='profesorForm'),
    path('profesorUpdate/<id_profesor>/', profesorUpdate, name='profesorUpdate'),
    path('profesorDelete/<id_profesor>/', profesorDelete, name='profesorDelete'),

    #Estudiantes

    path('estudiantes/', estudiantes, name='estudiantes'),
    path('estudiantes/', EstudianteList.as_view(), name='estudiantes'),

    path('entregables/', entregables, name='entregables'),
    path('acerca/', acerca, name='acerca'),



    path('buscarCursos/', buscarCursos, name='buscarCursos'),
    path('encontrarCursos/', encontrarCursos, name="encontrarCursos"),
    ]
