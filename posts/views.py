"""Posts views"""

#Django
#from django.shortcuts import render,redirect #ahora utilizamos render envez de HttpResponse pero igual recive un request
#from django.contrib.auth.decorators import login_required #para dentrar a un URL siempre y cuando este logueado (login requerido)
from django.contrib.auth.mixins import LoginRequiredMixin #REQUIERE DE LOGIN (OSEA DE ESTAR LOGUEADO)
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy

#Forms
from posts.forms import PostForm

#Models
from posts.models import Post

#Utilities
#from datetime import datetime

"""posts = [
	{
		'title':'Juan Daniel',
		'user':{
			'name':'Juancho',
			'picture':'https://picsum.photos/60/60/?random'
		},
		'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo':'https://picsum.photos/400/300/?random',
	},
	{
		'title':'Juan Daniel',
		'user':{
			'name':'Juancho',
			'picture':'https://picsum.photos/60/60/?random'
		},
		'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo':'https://picsum.photos/300/400/?random',
	},
	{
		'title':'Juan Daniel',
		'user':{
			'name':'Juancho',
			'picture':'https://picsum.photos/60/60/?random'
		},
		'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo':'https://picsum.photos/400/300/?random',
	},
	{
		'title':'Juan Daniel',
		'user':{
			'name':'Juancho',
			'picture':'https://picsum.photos/60/60/?random'
		},
		'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo':'https://picsum.photos/300/400/?random',
	},
	{
		'title':'Juan Daniel',
		'user':{
			'name':'Juancho',
			'picture':'https://picsum.photos/60/60/?random'
		},
		'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo':'https://picsum.photos/400/300/?random',
	}
]"""


# @login_required #DECORADOR que requiere estar logueado para entrar a feed.html (osea no deja entrar a la URL posts )
# def list_posts(request):
# 	"""List existing posts"""
# 	posts = Post.objects.all().order_by('-created') #TRAE TODOS LOS POST DEL DB
# 	return render(request, 'posts/feed.html',{'posts':posts}) #render(request, los html q hay en el file templates, contexto q son diccionarios)

#PARA MOSTRAR TODOS LOS POST EN EL FEED
class PostsFeedView(LoginRequiredMixin, ListView): #REMPLAZA EL 'def list_post' para listar todos los posts
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


# @login_required
# def create_post(request):
#     """Create new post view."""
#     if request.method == 'POST': #verifica q hayga informacion en POST
#         form = PostForm(request.POST, request.FILES) #LLAMA DEL FORMS DE POST "MODEL FORM"
#         if form.is_valid():
#             form.save()
#             return redirect('posts:feed')

#     else:
#         form = PostForm()

#     return render(
#         request=request,
#         template_name='posts/new.html',
#         context={
#             'form': form,
#             'user': request.user,
#             'profile': request.user.profile
#         }
#     )

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/new.html' #dice q template usamos
    form_class = PostForm #dice q formularios estamos usando
    success_url = reverse_lazy('posts:feed') #dice a donde nos redirigiremos

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context








"""{% extends "base.html" %} #HEREDA DE base.hmtl y se EJECUTA PRIMERO

{% block head_content %} #el contenido de este block va llenar a base.html donde lo pida con este mismo nombre de block
<title>Platzigram feed</title>
{% endblock %}

{% block container %} #el contenido de este block va llenar a base.html 
    <div class="row">
        {% for post in posts %}
        <div class="col-lg-4 offset-lg-4">
            <div class="media">
                <img class="mr-3 rounded-circle" src="{{ post.user.picture }}" alt="{{ post.user.name }}">
                <div class="media-body">
                    <h5 class="mt-0">{{ post.user.name }}</h5>
                    {{ post.timestamp }}
                </div>
            </div>
            <img class="img-fluid mt-3 border rounded" src="{{ post.photo }}" alt="{{ post.title }}">
            <h6 class="ml-1 mt-1">{{ post.title }}</h6>
        </div>
        {% endfor %}
    </div>
{% endblock %}"""




"""
de feed.html:
	{% for post in posts %}
    <div class="col-sm-12 col-md-8 offset-md-2 mt-5 p-0 post-container">
        <!--DATOS DEL USUARIO-->
        <div class="media pt-3 pl-3 pb-1">
            <a href="{% url "users:detail" post.user.username %}">
                <img class="mr-3 rounded-circle" height="35" src="{{ post.profile.picture.url }}" alt="{{ post.user.get_full_name }}">
            </a>
            
            <div class="media-body">
                <p style="margin-top: 5px;">{{ post.user.get_full_name  }}</p>
            </div>
        </div>
        
        <!--IMAGEN-->
        <img style="width: 100%;" src="{{ post.photo.url }}" alt="{{ post.title }}">
        <!--PUBLICO-->
        <p class="mt-1 ml-2" >
            <a href="" style="color: #000; font-size: 20px;">
                <i class="far fa-heart"></i>
            </a> 30 likes
        </p>
        <!--FECHA DE CREACION-->
        <p class="ml-2 mt-0 mb-2">
            <b>{{ post.title }}</b> - <small>{{ post.created }}</small>
        </p>
    </div>
    {% endfor %}
"""

