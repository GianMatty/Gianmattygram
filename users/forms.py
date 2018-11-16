"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Models
from django.contrib.auth.models import User
from users.models import Profile  

#PARA LOS FORMULARIOS
class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    #https://docs.djangoproject.com/es/2.1/ref/forms/validation/#cleaning-a-specific-field-attribute (validar formulario)
    def clean_username(self): #para validar los fields(clean_nombreField) (valida el campo con el DB)
        """Username must be unique."""
        username = self.cleaned_data['username'] #regresa la data limpia
        username_taken = User.objects.filter(username=username).exists() #exist: para q retorne un bool (verifica si existe el username)
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self): #para validar 2 campos propio de aqui (password y password confirmarion)
        """Verify password confirmation match."""
        data = super().clean() #default

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    #GUARDANDO O INSTANCIANDO TODOS LOS DATOS INGRESADOS UNA VEZ Q TODO ES VALIDO
    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation') #con pop se saca ese dato por q no sirve para llenar el model solo para validar

        user = User.objects.create_user(**data) #con los ** trae todo el diccionario y lo llena para instanciar al usuario
        profile = Profile(user=user) #profile solo tiene un solo valor para instanciar q es user (no hay phone,biography, etc)
        profile.save()


#CON LA IMPLEMENTACION DEL UpdateView YA NO SE NECESITA DE ESTE FORM PARA ACTUALIZAR PERFIL
# class ProfileForm(forms.Form): #envia a quien lo llame mediante una instanciacion
#     """Profile form."""

#     website = forms.URLField(max_length=200, required=True)
#     biography = forms.CharField(max_length=500, required=False)
#     phone_number = forms.CharField(max_length=20, required=False)
#     picture = forms.ImageField()