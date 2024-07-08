
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from entidades.models import *

from .forms import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Modelando estudiantes con CBV
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

#decoradores
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.



# Create your views here.
def home(request):
    return render(request, "entidades/index.html")

#___Cursos
@login_required
def cursos(request):
    contexto = {"cursos": Curso.objects.all()}
    return render(request, "entidades/cursos.html", contexto)
@login_required
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
@login_required
def cursoUpdate(request, id_curso):
    curso = Curso.objects.get(id=id_curso)
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso.nombre = miForm.cleaned_data["nombre"]
            curso.comision = miForm.cleaned_data["comision"]
            curso.save()
            contexto = {"cursos": Curso.objects.all()}
            return render(request, "entidades/cursos.html", contexto)
    else:
        miForm = CursoForm(initial={"nombre": curso.nombre, "comision": curso.comision})

    return render(request, "entidades/cursoForm.html", {"form":miForm})
@login_required
def cursoDelete(request, id_curso):
    curso = Curso.objects.get(id=id_curso)
    curso.delete()
    contexto = {"cursos": Curso.objects.all()}
    return render(request, "entidades/cursos.html", contexto)

@login_required
#___ Profesores
def profesores(request):
    contexto = {"profesores": Profesor.objects.all()}
    return render(request, "entidades/profesores.html", contexto)
@login_required
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
@login_required
def profesorUpdate(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    if request.method == "POST":
        miForm = ProfesorForm(request.POST)
        if miForm.is_valid():
            profesor.nombre = miForm.cleaned_data["nombre"]
            profesor.apellido = miForm.cleaned_data["apellido"]
            profesor.email = miForm.cleaned_data["email"]
            profesor.profesion = miForm.cleaned_data["profesion"]
            profesor.save()
            contexto = {"profesores": Profesor.objects.all()}
            return render(request, "entidades/profesores.html", contexto)
    else:
        miForm = ProfesorForm(initial={"nombre": profesor.nombre, "apellido": profesor.apellido, "email": profesor.email, "profesion": profesor.profesion})

    return render(request, "entidades/profesorForm.html", {"form":miForm})
@login_required
def profesorDelete(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    profesor.delete()
    contexto = {"profesores": Profesor.objects.all()}
    return render(request, "entidades/profesores.html", contexto)


#___Estudiante.

class EstudianteList(LoginRequiredMixin, ListView):
    model = Estudiante

class EstudianteCreate(LoginRequiredMixin, CreateView):
    model = Estudiante
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("estudiantes")

class EstudianteUpdate(LoginRequiredMixin, UpdateView):
    model = Estudiante
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("estudiantes")
class EstudianteDelete(LoginRequiredMixin, DeleteView):
    model = Estudiante
    success_url = reverse_lazy("estudiantes")



#def estudiantes(request):
 #   contexto = {"estudiantes": Estudiante.objects.all()}
  #  return render(request, "entidades/estudiantes.html", contexto)
#No hace falta porque esta resuelta con el cbv


@login_required
def entregables(request):
    contexto = {"entregables": Entregable.objects.all()}
    return render(request, "entidades/entregables.html", contexto)



def acerca(request):
    return render(request, "entidades/acerca.html")

#__buscar
@login_required
def buscarCursos(request):
	return render(request, "entidades/buscar.html")

@login_required
def encontrarCursos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        cursos = Curso.objects.filter(nombre__icontains=patron)
        contexto = {"cursos": cursos}
    else:
        contexto = {"cursos": Curso.objects.all()}

    return render(request, "entidades/cursos.html", contexto)


# Login - Logout - Registration

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return render(request, "entidades/index.html")
        else:
            return redirect(reverse_lazy('login'))

    else:
        miForm = AuthenticationForm()

    return render(request, "entidades/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()
    return render(request, "entidades/registro.html", {"form": miForm})