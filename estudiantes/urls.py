from django.urls import path
from . import views

app_name = 'estudiantes'
urlpatterns = [
    path('', views.listaEstudiantes, name='listaEstudiantes')
    ]