from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
        path('biblioteca/', include('biblioteca.urls', namespace='sitio')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
