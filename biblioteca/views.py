from django.shortcuts import render
from .models import Libro
from django.views.generic.edit import CreateView
from biblioteca.forms import FormCrearLibro

def books(request):
	all_books = Libro.objects.all() 
	context = {'object_list':all_books}
	return render(request, 'biblioteca/allbooks.html', context)

class LibroCreateView(CreateView):
	model = Libro
	form_class = FormCrearLibro 
	template_name = 'biblioteca/crearlibro.html'