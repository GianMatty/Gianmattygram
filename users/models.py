"""Users models"""

#Django
from django.contrib.auth.models import User #importamos el User(tabla de django por defecto) para extenderlo
from django.db import models

class Profile(models.Model):
	"""Profile model"""

	#PROXY MODEL para extender mas information de la tabla User
	user = models.OneToOneField(User, on_delete=models.CASCADE) #para q herede los campos de User

	#aumentamos mas campos al User
	website = models.URLField(max_length=200, blank=True)
	biography = models.TextField(blank=True)
	phone_number = models.CharField(max_length=20, blank=True)

	picture = models.ImageField( 
 		upload_to='users/pictures', #ruta donde se guarda la imagen (en el folder 'media')
    	blank=True, 
    	null=True
    )

	created = models.DateTimeField(auto_now_add=True) # guarda la fecha en q se crea esta instancia User
	modified = models.DateTimeField(auto_now=True) # guarda la fecha en q se hizo la ultima modificacion

	
	def __str__(self): # imprime solo el email por defecto cuando llame a los registros 
		"""Return usarname"""
		return self.user.username

