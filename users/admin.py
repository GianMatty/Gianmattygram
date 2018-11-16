"""User admin"""

#Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
#Models
from django.contrib.auth.models import User
from users.models import Profile


# Register your models here.
#admin.site.register(Profile) #para registrar nuestro modelo Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	"""Profile admin."""

	list_display = ('pk', 'user', 'phone_number', 'website', 'picture') #para que se muestre
	list_display_links = ('pk', 'user',) #para que se pueda linkear
	#list_editable = ('phone_number', 'website', 'picture') #para q se pueda editar al instante

	search_fields = ( #para que se puede buscar por estos campos
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

	list_filter = ( #para que se puede filtrar por estos campos
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )

	fieldsets = ( #para modificar los datos luego de linkear
        ('Profile',{
            'fields':(('user','picture'),)
        }),
        ('Extra info',{
            'fields':(
                ('website','phone_number'),
                ('biography'),
            )
        }),
        ('Metadata',{
            'fields':(('created','modified'),),
        })
    )
	readonly_fields = ('created','modified') #datos q nose pueden modificar solo muestran sus valores


class ProfileInline(admin.StackedInline):
	"""profile in-line admin for users"""
	
	model = Profile
	can_delete = False
	verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
	"""Add profile admin to base user admin"""

	inlines = (ProfileInline,)
	list_display = (
    	'username',
    	'email',
    	'first_name',
    	'last_name',
    	'is_active',
    	'is_staff'
	)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
