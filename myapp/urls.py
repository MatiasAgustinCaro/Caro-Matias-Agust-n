from django.urls import path
from .views import inicio, acerca, Libros, crear, editar, borrar, registro
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',inicio, name= "Inicio"),
    path('acerca/',acerca, name='acerca'),
    path('biblioteca/',Libros, name="libros"),
    path('biblioteca/crear',crear, name='crear'),
    path('biblioteca/editar/<int:id>',editar, name='editar'),
    path('biblioteca/delete/<int:id>',borrar, name='delete'),
    path('registro/', registro, name="registro")
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)