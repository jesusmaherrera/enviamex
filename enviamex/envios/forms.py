#encoding:utf-8
from django import forms

import autocomplete_light
from cities_light.models import City
from models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, AdminPasswordChangeForm
from django.forms.models import BaseInlineFormSet, inlineformset_factory

class PerfilUsarioManageForm(forms.ModelForm):
    class Meta:
        widgets = autocomplete_light.get_widgets_dict(PerfilUsario)
        model = PerfilUsario
        exclude = ('usuario',)
        
class PerfilClienteManageForm(forms.ModelForm):
    
    class Meta:
        widgets = autocomplete_light.get_widgets_dict(PerfilUsario)
        model = PerfilUsario
        exclude = ('usuario','tipo',)

class EnvioManageForm(forms.ModelForm):
	class Meta:
		model = Envio

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", )

class UsarioChangeForm(forms.ModelForm):
    username = forms.RegexField(label="Nombre de Usuario", max_length=30, regex=r'^[\w.@+-]+$',
        help_text = "Maximo. 30 caracteres. letras, digitos y @/./+/-/_ solamente.",
        error_messages = {'invalid': "Este campo solo puede contener letras, numeros y caracteres '@/./+/-/_' "})
    new_password1   = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput, required=False)
    new_password2   = forms.CharField(label="Confirma Nueva Contraseña", widget=forms.PasswordInput, required=False)
    email           = forms.CharField(required=True)
    class Meta(UserChangeForm):
        model = User
        exclude = ('password', 'last_login', 'date_joined','last_name','first_name','is_superuser','groups','user_permissions','is_active',"is_staff",)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        #else:
         #   if len(password2) > 0 and len(password2) < 8:
          #      raise forms.ValidationError("Your password must be a minimum of 8 characters.")
        return password2

    def save(self, commit=True):
        user = super(UsarioChangeForm, self).save(commit=False)
        if len(self.cleaned_data['new_password2']) > 0:
            user.set_password(self.cleaned_data['new_password2'])
        if commit:
        	if user.is_staff:
        		user.is_superuser = True
        		
        	if user.username == 'admin':
        		user.is_staff = True

        	user.save()
        return user

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email" )

class CiudadManageForm(forms.ModelForm):
    class Meta:
        model = City
        exclude = (
            'latitude',
            'longitude',
            'alternate_names',
            'geoname_id',
            'name_ascii',
            )