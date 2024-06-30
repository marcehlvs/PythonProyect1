
from django.shortcuts import render

from entidades.models import *

from .forms import *
# Create your views here.



# Create your views here.
def home(request):
    return render(request, "entidades/index.html")
def cursos(request):
    contexto = {"cursos": Curso.objects.all()}
    return render(request, "entidades/cursos.html", contexto)
def profesores(request):
    contexto = {"profesores": Profesor.objects.all()}
    return render(request, "entidades/profesores.html", contexto)
def estudiantes(request):
    contexto = {"estudiantes": Estudiante.objects.all()}
    return render(request, "entidades/estudiantes.html", contexto)
def entregables(request):
    contexto = {"entregables": Entregable.objects.all()}
    return render(request, "entidades/entregables.html", contexto)
def acerca(request):
    return render(request, "entidades/acerca.html")

#formularios

def cursoForm(request):
    if request.method == "POST": #¿Es la primera vez que viene el formulario? ¿Ya vienen los datos cargados?
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso_nombre = miForm.cleaned_data["nombre"]
            curso_comision = miForm.cleaned_data["comision"]
            curso = Curso(nombre=curso_nombre, comision=curso_comision)
            curso.save()
            contexto = {"cursos": Curso.objects.all()}
            return render(request, "entidades/cursos.html", contexto)
    else:
        miForm = CursoForm()
    return render(request, "entidades/cursoForm.html", {"form": miForm})

def profesorForm(request):
    if request.method == "POST": #¿Es la primera vez que viene el formulario? ¿Ya vienen los datos cargados?
        miForm = ProfesorForm(request.POST)
        if miForm.is_valid():
            profe_nombre = miForm.cleaned_data["nombre"]
            profe_apellido = miForm.cleaned_data["apellido"]
            profe_email = miForm.cleaned_data["email"]
            profe_profesion = miForm.cleaned_data["profesion"]
            profesor = Profesor(nombre=profe_nombre, apellido=profe_apellido, email=profe_email, profesion = profe_profesion)
            profesor.save()
            contexto = {"profesores": Profesor.objects.all()}
            return render(request, "entidades/profesores.html", contexto)
    else:
        miForm = ProfesorForm()
    return render(request, "entidades/profesorForm.html", {"form": miForm})


#__buscar

def buscarCursos(request):
	return render(request, "entidades/buscar.html")


def encontrarCursos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        cursos = Curso.objects.filter(nombre__icontains=patron)
        contexto = {"cursos": cursos}
    else:
        contexto = {"cursos": Curso.objects.all()}

    return render(request, "entidades/cursos.html", contexto)
