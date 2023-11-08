from django.shortcuts import render
from .models import Estudiante

def listaEstudiantes(request):
    estudiantes = Estudiante.objects.filter()
    return render(request,
                  'estudiantes/estudiantes.html',
                  {'estudiantes': estudiantes})