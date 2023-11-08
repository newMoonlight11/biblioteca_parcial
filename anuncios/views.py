from django.shortcuts import render
from .models import Anuncio

def listadoAnuncios(request):
    anuncios = Anuncio.objects.filter(estado="activo")
    return render(request,
                  'anuncios/anuncios.html',
                  {'anuncios': anuncios})
