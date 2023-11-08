from django.shortcuts import render
from .models import Libro

def books(request):
    all_books = Libro.objects.all()
    context = {'object_list':all_books}
    return render(request, 'biblioteca/allboks.html', context)


def detail_book(request, id_book):
    book = Libro.objects.get(id=id_book)
    context = {'object':book}
    return render(request, 'biblioteca/detailbook.html', context)

# Create your views here.
