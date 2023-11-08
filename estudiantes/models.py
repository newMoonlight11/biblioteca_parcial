from django.db import models

class Estudiante(models.Model):
    CARRERAS = (
        ('Medicina', 'Medicina'),
        ('Enfermería', 'Enfermería'),
        ('Administración de Empresas', 'Administración de Empresas'),
        ('Contaduría Pública', 'Contaduría Pública'),
        ('Economía', 'Economía'),
        ('Derecho', 'Derecho'),
        ('Ingeniería Biomédica', 'Ingeniería Biomédica'),
        ('Ingeniería de Sistemas', 'Ingeniería de Sistemas'),
        ('Ingeniería Financiera', 'Ingeniería Financiera'),
        ('Ingeniería de Mercados', 'Ingeniería de Mercados'),
        ('Ingeniería en Energía', 'Ingeniería en Energía'),
        ('Ingeniería Mecatrónica', 'Ingeniería Mecatrónica'),
        ('Ingeniería Industrial', 'Ingeniería Industrial')
    )
    SANGRE = (
        ('O negativo', 'O negativo'),
        ('O positivo', 'O positivo'),
        ('A negativo', 'A negativo'),
        ('A positivo', 'A positivo'),
        ('B negativo', 'B negativo'),
        ('B positivo', 'B positivo'),
        ('AB negativo', 'AB negativo'),
        ('AB positivo', 'AB positivo')
    )
    SEXO = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro')
    )
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    cedula = models.CharField(max_length=100)
    uid = models.CharField(max_length=100)
    genero = models.CharField(choices=SEXO, max_length=20)
    sangre = models.CharField(choices=SANGRE, max_length=20)
    email = models.EmailField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    carrera = models.CharField(choices=CARRERAS, max_length=50)
    semestre = models.IntegerField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        cadena=self.nombres+" "+self.apellidos
        return cadena
        