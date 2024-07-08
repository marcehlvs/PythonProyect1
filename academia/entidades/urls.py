from django.urls import path, include
from entidades.views import *

from django.contrib.auth.views import LogoutView



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

    path('estudiantes/', EstudianteList.as_view(), name='estudiantes'),
    path('estudianteCreate/', EstudianteCreate.as_view(), name='estudianteCreate'),
    path('estudianteUpdate/<int:pk>/', EstudianteUpdate.as_view(), name='estudianteUpdate'),
    path('estudianteDelete/<int:pk>/', EstudianteDelete.as_view(), name='estudianteDelete'),



    path('entregables/', entregables, name='entregables'),
    path('acerca/', acerca, name='acerca'),

    #buscar

    path('buscarCursos/', buscarCursos, name='buscarCursos'),
    path('encontrarCursos/', encontrarCursos, name="encontrarCursos"),

    #login/logout/registration

    path('login/', loginRequest, name='login'),
    path('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name="logout"),

    #registro
    path('registro/', register, name="registro"),
    ]