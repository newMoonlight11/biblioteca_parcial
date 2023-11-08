from django.contrib import admin
from .models import Editor, Autor, Libro

admin.site.register(Editor)
admin.site.register(Autor)
admin.site.register(Libro)