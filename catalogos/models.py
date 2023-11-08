from django.db import models

class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    fechaNacimiento = models.DateField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        cadena=self.nombre+" "+self.apellido
        return cadena