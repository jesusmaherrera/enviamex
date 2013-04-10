#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from models import *
from forms import *
import datetime, time

#Paginacion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# user autentication
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, AdminPasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required


def index(request):
  	return render_to_response('index.html', {}, context_instance=RequestContext(request))

def envios_View(request, template_name='envios/envios.html'):
	envios = Envio.objects.all
	c = {'envios':envios}
	return render_to_response(template_name, c, context_instance=RequestContext(request))

def clientes_View(request, template_name='clientes/clientes.html'):
	clientes = Cliente.objects.all
	c = {'clientes':clientes}
	return render_to_response(template_name, c, context_instance=RequestContext(request))

def cliente_manageView(request, id = None, template_name='clientes/cliente.html'):
	if id:
		cliente = get_object_or_404(Cliente, pk=id)
	else:
		cliente = Cliente()

	msg = '' 

	if request.method == 'POST':
		Cliente_form = ClienteManageForm(request.POST, request.FILES, instance=cliente)

		if Cliente_form.is_valid():
			Cliente_form.save()
			return HttpResponseRedirect('/clientes/')
	else:
		Cliente_form = ClienteManageForm(instance=cliente)
		
	c = {'cliente_form': Cliente_form, }

	return render_to_response(template_name, c, context_instance=RequestContext(request))

def cliente_deleteView(request, id = None):
	cliente = get_object_or_404(Cliente, pk=id)
	cliente.delete()

	return HttpResponseRedirect('/clientes/')