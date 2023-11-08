from django import forms
from biblioteca.models import Libro


class FormCrearLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autores', 'editor', 'fecha_publicacion', 'imagen', 'resumen','isbn']
        