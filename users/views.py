"""Users views"""

#Django
#from django.contrib.auth import authenticate, login, logout #libreria para autenticar,login y logout 
from django.contrib.auth import views as auth_views #authenticar las vistas
from django.contrib.auth.decorators import login_required #para dentrar a un URL siempre q hayga un login (login requerido)
from django.contrib.auth.mixins import LoginRequiredMixin #requiere estar loqueado
#from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy #construye una url

from django.views.generic import DetailView, FormView, UpdateView
#from django.views.generic import TemplateView #VISTAS BASADAS EN CLASES

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

#forms
#from users.forms import ProfileForm
from users.forms import SignupForm #(import nombreForm)import los campos de 'Form'

"""
# Exception
from django.db.utils import IntegrityError

# Models
from users.models import Profile  
""" 


#PARA LOS DETALLES DE UN PERFIL
class UserDetailView(LoginRequiredMixin, DetailView): # #antes (TemplateVIew) VISTAS BASADAS EN CLASES
    """User detail view."""

    template_name = 'users/detail.html' #template_name: es el enlace al html
    slug_field = 'username'
    slug_url_kwarg = 'username' #es de '<str:username>' de las urls
    queryset = User.objects.all()
    context_object_name = 'user' #define el nombre del objeto q traigamos

    def get_context_data(self, **kwargs): #agraga datos al contexto
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context
   


# def login_view(request):
# 	"""Login view"""

# 	#https://docs.djangoproject.com/en/2.1/topics/auth/default/#auth-web-requests #link a documentacion de login
# 	if request.method == 'POST': #verifica si hay datos en POST
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(request, username=username, password=password)
# 		if user:
# 			login(request, user)
# 			return redirect('posts:feed') #redirecciona al URL (name='feed'('posts/'))
# 		else:
# 			return render(request, 'users/login.html', {'error': 'Invalid username and password'})

# 	return render(request, 'users/login.html')

class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html' #en el setting config: LOGIN_REDIRECT_URL = '/'


# @login_required #requiere estar logueado para entrar a esto
# def logout_view(request):
# 	"""Logout a user"""

# 	#https://docs.djangoproject.com/es/2.1/topics/auth/default/#how-to-log-a-user-out #link a documentacion de logout
# 	logout(request)
# 	return redirect('users:login')

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
 
    template_name = 'users/logged_out.html' #nombre predetermina de html (documentacion de django) https://docs.djangoproject.com/es/2.1/topics/auth/default/#all-authentication-views

# def signup(request):
#     """Sign up view."""

#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users:login')
#     else:
#         form = SignupForm()

#     return render(
#         request=request,
#         template_name='users/signup.html',
#         context={'form': form}
#     )

class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html'
    form_class = SignupForm #trae un formulario
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form) #retornamos el formulario


    
# @login_required
# def update_profile(request):
#     """Update a user's profile view."""
#     profile = request.user.profile

#     if request.method == 'POST': #verifica si hay datos en POST
#         form = ProfileForm(request.POST, request.FILES) #Instancia un formulario #request.POST: trae los datos normales #request.FILES: tra los archivos media
#         if form.is_valid():
#             data = form.cleaned_data #trae y limpia la data

#             profile.website = data['website']
#             profile.phone_number = data['phone_number']
#             profile.biography = data['biography']
#             profile.picture = data['picture']
#             profile.save()

#             url = reverse('users:detail', kwargs={'usarname': request.user.username})
#             return redirect(url)

#     else:
#         form = ProfileForm() #instancia form vacio

#     return render(
#         request=request,
#         template_name='users/update_profile.html',
#         context={
#             'profile': profile, #manda los datos de profile (perfil del usuario)
#             'user': request.user, #manda los datos de request.user (usuario)
#             'form': form #manda los datos de form
#         }
#     )

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture'] #los fields q edita #con eso nos ahorramos el form

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})