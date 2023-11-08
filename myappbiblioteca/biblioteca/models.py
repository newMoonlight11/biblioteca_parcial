from django.db import models

class Editor(models.Model):
    direccion = models.CharField(max_length=50)

    ciudad = models.CharField(max_length=60)

    departamento = models.CharField(max_length=30)

    pais = models.CharField(max_length=50)

    website = models.URLField()



    def __str__(self):

        return self.nombre




class Autor(models.Model):

    nombre = models.CharField(max_length=30)

    apellido = models.CharField(max_length=40)

    email = models.EmailField(blank=True)



    def __str__(self):

        cadena = "%s %s" % (self.nombre, self.apellido)

        return cadena




class Libro(models.Model):

    titulo = models.CharField(max_length=100)

    autores = models.ManyToManyField(Autor)

    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)

    fecha_publicacion = models.DateField()

    imagen = models.ImageField(upload_to='photos/')

    resumen = models.TextField(blank=True)

    isbn = models.CharField(max_length=30)



    def __str__(self):

        return self.titulo
# Create your models here.
