from django.urls import path
from . import views 
app_name = 'biblioteca'
urlpatterns = [
    path('', views.books, name='index'),
    path('crearlibro/',views.LibroCreateView.as_view(), name='crear'),
]