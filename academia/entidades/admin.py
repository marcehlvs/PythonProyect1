from django.contrib import admin
from .models import *
# Register your models here.

class CursoAdmin(admin.ModelAdmin):
		list_display = ('nombre', 'comision')
		list_filter = ('nombre')
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'email', 'profesion')

admin.site.register(Curso)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Estudiante)
admin.site.register(Entregable)