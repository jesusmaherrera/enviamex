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

@login_required(login_url='/login/')
def envios_View(request, template_name='envios/envios.html'):
	envios = Envio.objects.all
	c = {'envios':envios}
	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def clientes_View(request, template_name='clientes/clientes.html'):
	clientes = Cliente.objects.all
	c = {'clientes':clientes}
	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
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

def clientenormal_manageView(request, id = None, template_name='clientes/clienteNormal.html'):
	if id:
		cliente = get_object_or_404(Cliente, pk=id)
	else:
		cliente = Cliente()
		usuario = User()
	msg = '' 

	if request.method == 'POST':
		Cliente_form = ClienteNormalManageForm(request.POST, request.FILES, instance=cliente)

		if Cliente_form.is_valid():
			Cliente_form.save()
			return HttpResponseRedirect('/clientes/')
	else:
		usuario_form = RegisterForm(instance= usuario)
		Cliente_form = ClienteNormalManageForm(instance=cliente)
		
	c = {'cliente_form': Cliente_form, 'usuario_form': usuario_form, }

	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def cliente_deleteView(request, id = None):
	cliente = get_object_or_404(Cliente, pk=id)
	cliente.delete()

	return HttpResponseRedirect('/clientes/')

@login_required(login_url='/login/')
def envio_manageView(request, id = None, template_name='envios/envio.html'):
	if id:
		envio = get_object_or_404(Envio, pk=id)
	else:
		envio = Envio()

	msg = '' 

	if request.method == 'POST':
		envio_form = EnvioManageForm(request.POST, request.FILES, instance=envio)

		if envio_form.is_valid():
			envio_form.save()
			return HttpResponseRedirect('/envios/')
	else:
		envio_form = EnvioManageForm(instance=envio)
		
	c = {'envio_form': envio_form, }

	return render_to_response(template_name, c, context_instance=RequestContext(request))

##########################################
## 										##
##              USUARIOS  			    ##
##										##
##########################################

def ingresar(request):
	# if not request.user.is_anonymous():
	# 	return HttpResponseRedirect('/')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/envios/')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('login.html',{'form':formulario, 'message':'Nombre de usaurio o password no validos',}, context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
	return render_to_response('login.html',{'form':formulario, 'message':'',}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')