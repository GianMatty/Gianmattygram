"""Users URLs."""

# Django
from django.urls import path
#from django.views.generic import TemplateView #VISTAS BASADAS EN CLASES

# View
from users import views


urlpatterns = [

    # Management
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update'
    ),           

    # Posts
    path(
        route='<str:username>/', # espera un argumento 'username' #es el 'slug_url_kwarg' de la clase
        #view=TemplateView.as_view(template_name='users/detail.html'),
        view=views.UserDetailView.as_view(), #VISTAS BASADAS EN CLASES (nombre_file.nombreDetailView.as_view)
        name='detail'
    )
]