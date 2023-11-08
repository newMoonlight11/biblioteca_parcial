from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('biblioteca.urls')),
        path('biblioteca/', include('biblioteca.urls', namespace='sitio')),
        path('anuncios/', include('anuncios.urls')),
        path('estudiantes/', include('estudiantes.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
