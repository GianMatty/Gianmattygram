"""Platzigram middleware catalog.""" #CREA RESTRICCIONES DESDE AQUI

# Django
from django.shortcuts import redirect
from django.urls import reverse

#https://docs.djangoproject.com/es/2.1/topics/http/middleware #documentation sobre middleware
class ProfileCompletionMiddleware: #segun la documentacion asi se crea un middleware (class nombreMiddleware:)
    """Profile completion middleware. (middleware para exigir q complete el perfil)

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous: #asegurar q haya un usuario logueado (is_anonimo= si esta logueado no(false))
            if not request.user.is_staff: #si no es un superusuario entra
                profile = request.user.profile #trae el perfil del usuario
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update'), reverse('users:logout')]: #con el logout el user se vuelve anonimo
                        return redirect('users:update')

        response = self.get_response(request) #CODIGO Q SE PARA EL ANTES Y DESPUES

        """Code to be executed for each request after that view is called."""
        return response

#LUEGO DE CREAR ESTE MIDDLEWARE SE TIENE Q DECLARAR EN LAS MIDDLEWARE DE SETTINGS