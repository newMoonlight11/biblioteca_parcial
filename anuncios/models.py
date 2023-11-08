from django.db import models

class Anuncio(models.Model):
    STATUS_CHOICES = (
        ('inactivo', 'Inactivo'),
        ('activo', 'Activo'),
    )
    titulo = models.CharField(max_length=150)
    texto = models.TextField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='inactivo')
    class Meta:
        ordering = ('-fechaCreacion',)
    def __str__(self):
        return self.titulo