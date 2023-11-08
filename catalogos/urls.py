from django.urls import path
from . import views 
app_name = 'catalogos'
urlpatterns = [
    path('', views.index, name='index'),
]