from django.urls import path
from . import views
app_name = 'anuncios'
urlpatterns = [
    path('', views.listadoAnuncios, name='listadoAnuncios')
]
