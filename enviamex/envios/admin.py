import autocomplete_light
from models import *
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import User

# class EmployeeInline(admin.StackedInline):
#     model = UserProfile
#     can_delete = False
#     verbose_name_plural = 'Perfil de usuario'

# # Define a new User admin
# class UserAdmin(UserAdmin):
#     inlines = (EmployeeInline, )

admin.site.register(PerfilUsario)
admin.site.register(Envio)

# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User)
#admin.site.register(UserProfile)