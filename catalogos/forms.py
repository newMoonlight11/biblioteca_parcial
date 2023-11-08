from django import forms
from datetime import datetime
from .models import Usuarios

class RegistrarUsuario(forms.Form):
    nombre = forms.CharField(label='Nombre:',max_length=50,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Nombre',
                                    }))
    apellido = forms.CharField(label='Apellido:',max_length=50,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Apellido',
                                    }))
    telefono = forms.CharField(label='Teléfono',max_length=12,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Telefono',
                                    }))
    fechaNacimiento = forms.DateField(label='Fecha de nacimiento:',
                                    widget=forms.SelectDateWidget(years=range(1920,2021),
                                    attrs={
                                        'class':'form-control',
                                    }))
    email = forms.EmailField(label='Email:',max_length=254,
                                    widget=forms.EmailInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'ejemplo@ejemplo.com',
                                    }))

def registrar_usuario(self):
        fecha = datetime(int(self.data['fechaNacimiento_year']),
                        int(self.data['fechaNacimiento_month']),
                        int(self.data['fechaNacimiento_day']))
        
        nuevo_usuario = Usuarios(nombre=self.data['nombre'],apellido=self.data['apellido'],
                        telefono=self.data['telefono'],
                        fechaNacimiento=fecha,
                        email=self.data['email'])
        nuevo_usuario.save()
        return 'Registro exitoso'