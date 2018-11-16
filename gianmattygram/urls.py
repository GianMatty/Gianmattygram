
#Django
from django.contrib import admin #para que administre los usuarios
from django.urls import path, include #default

from django.conf.urls.static import static #para la media
from django.conf import settings #para la media


urlpatterns = [
	path('admin/', admin.site.urls), # incluir todas las URLs de admin

	path('', include(('posts.urls', 'posts'), namespace='posts')), #path('ruta_inicial', include())
    path('users/', include(('users.urls', 'users'), namespace='users')), #include(('ruta_urls','nombre_app'), namespace)

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para la media

