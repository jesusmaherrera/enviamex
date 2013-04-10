#encoding:utf-8
from django import forms

import autocomplete_light

from models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, AdminPasswordChangeForm
from django.forms.models import BaseInlineFormSet, inlineformset_factory

class ClienteManageForm(forms.ModelForm):
	class Meta:
		model = Cliente