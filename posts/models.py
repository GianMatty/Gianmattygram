"""Posts models."""

# Django
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Post model."""

    #para relacionar un usuario con un post
    user = models.ForeignKey(User, on_delete=models.CASCADE) #CASCADE para q cuando se borre un usuariop se borre los posts
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE) # 'nombre_apps.model' = 'users.Profile' (tbn es valido)


    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)
        #return f'{self.title} by @{self.user.username}'