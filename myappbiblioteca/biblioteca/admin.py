from django.contrib import admin
from .models import Editor, Autor, Libro

admin.site.register(Editor)
admin.site.register(Libro)
admin.site.register(Autor)
# Register your models here.
