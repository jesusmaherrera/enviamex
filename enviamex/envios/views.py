#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from models import *
from forms import *
import datetime, time
from django.contrib.auth.models import User
#Paginacion
from cities_light.models import City
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# user autentication
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, AdminPasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required

def dineroView(request):
  	return render_to_response('dinero.html', {}, context_instance=RequestContext(request))

def recepcionView(request):
  	return render_to_response('recepcion.html', {}, context_instance=RequestContext(request))

def serviciosView(request):
  	return render_to_response('servicios.html', {}, context_instance=RequestContext(request))

def contactoView(request):
  	return render_to_response('contacto.html', {}, context_instance=RequestContext(request))

def index(request):
  	return render_to_response('index.html', {}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def envios_View(request, template_name='envios/envios.html'):
	if request.user.is_staff:
		envios = Envio.objects.all
	else:
		envios = Envio.objects.filter(usuario=request.user) 

	c = {'envios':envios}
	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def envio_deleteView(request, id = None):
	if request.user.is_staff:
		envio = get_object_or_404(Envio, pk=id)
		envio.delete()

	return HttpResponseRedirect('/envios/')

@login_required(login_url='/login/')
def clientes_View(request, template_name='clientes/clientes.html'):
	if request.user.is_staff:
		clientes = PerfilUsario.objects.all
	else:
		return HttpResponseRedirect('/envios/')

	c = {'clientes':clientes}
	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def usuario_manageView(request, id = None, template_name='clientes/usuario.html'):
	nuevousuario = False
	if id:
		perfil_usario = get_object_or_404(PerfilUsario, pk=id)
		usuario = perfil_usario.usuario
	else:
		nuevousuario = True
		perfil_usario = PerfilUsario()
		usuario = User()

	msg = '' 

	if request.method == 'POST':
		if nuevousuario:
			usuario_form = RegisterForm(request.POST, request.FILES, instance=usuario)
		else:			
			usuario_form = UsarioChangeForm(request.POST, request.FILES, instance=usuario)

		perfil_usarioForm = PerfilUsarioManageForm(request.POST, request.FILES, instance=perfil_usario)
		
		if perfil_usarioForm.is_valid() and usuario_form.is_valid():
			perfil = perfil_usarioForm.save(commit=False)
			if perfil.tipo == 'A':
				usuario.is_staff = True
			else:
				usuario.is_staff = False

			usuario = usuario_form.save()
			perfil.usuario = usuario
			perfil_usarioForm.save()

			return HttpResponseRedirect('/clientes/')
	else:
		perfil_usarioForm = PerfilUsarioManageForm(instance=perfil_usario)
		if nuevousuario:
			usuario_form = RegisterForm(instance= usuario)
		else:
			usuario_form = UsarioChangeForm(instance=usuario)

	c = {'perfil_usarioForm': perfil_usarioForm, 'usuario_form': usuario_form, }

	return render_to_response(template_name, c, context_instance=RequestContext(request))

def cliente_manageView(request, id = None, template_name='clientes/cliente.html'):
	nuevousuario = False
	if id:
		perfil_usario = get_object_or_404(PerfilUsario, pk=id)
		usuario = perfil_usario.usuario
	else:
		nuevousuario = True
		perfil_usario = PerfilUsario()
		usuario = User()

	msg = '' 

	if request.method == 'POST':
		if nuevousuario:
			usuario_form = RegisterForm(request.POST, request.FILES, instance=usuario)
		else:			
			usuario_form = UsarioChangeForm(request.POST, request.FILES, instance=usuario)

		perfil_usarioForm = PerfilClienteManageForm(request.POST, request.FILES, instance=perfil_usario)
		
		if perfil_usarioForm.is_valid() and usuario_form.is_valid():
			perfil = perfil_usarioForm.save(commit=False)
			usuario.is_staff = False
			usuario = usuario_form.save()

			perfil.usuario = usuario
			perfil_usarioForm.save()

			return HttpResponseRedirect('/clientes/')
	else:
		perfil_usarioForm = PerfilClienteManageForm(instance=perfil_usario)
		if nuevousuario:
			usuario_form = RegisterForm(instance= usuario)
		else:
			usuario_form = UsarioChangeForm(instance=usuario)

	c = {'perfil_usarioForm': perfil_usarioForm, 'usuario_form': usuario_form, }

	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def usuario_deleteView(request, id = None):
	if request.user.is_staff:
		
		perfil_usario = get_object_or_404(PerfilUsario, pk=id)
		usuario = get_object_or_404(User, pk=perfil_usario.usuario.id)
		if not usuario.username == 'admin':
			usuario.delete()
			perfil_usario.delete()
			
	return HttpResponseRedirect('/clientes/')

@login_required(login_url='/login/')
def envio_manageView(request, id = None, template_name='envios/envio.html'):
	if request.user.is_staff:
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
	else:
		return HttpResponseRedirect('/envios/')
		
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


##########################################
## 										##
##               CIUDAD  			    ##
##										##
##########################################

@login_required(login_url='/login/')
def ciudad_manageView(request, id = None, template_name='ciudades/ciudad.html'):
	if id:
		ciudad = get_object_or_404(City, pk=id)
	else:
		ciudad = City()

	if request.method == 'POST':
		Ciudad_form = CiudadManageForm(request.POST, request.FILES, instance=ciudad)

		if Ciudad_form.is_valid():
			if request.user.has_perm('envios.change_city'):
				Ciudad_form.save()
			
			return HttpResponseRedirect('/ciudades/')
	else:
		if request.user.has_perm('envios.add_city'):
			Ciudad_form = CiudadManageForm(instance=ciudad)
		else:
			return HttpResponseRedirect('/ciudades/')

	c = {'ciudad_form': Ciudad_form, }

	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def ciudades_View(request, template_name='ciudades/ciudades.html'):
	try: 
		filtro = request.GET['filtro']
	except:
		filtro = ''
	ciudades_list = City.objects.filter(name__icontains=filtro).filter(country__name='Mexico')

	paginator = Paginator(ciudades_list, 20) # Muestra 5 inventarios por pagina
	page = request.GET.get('page')

	#####PARA PAGINACION##############
	try:
		ciudades = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    ciudades = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    ciudades = paginator.page(paginator.num_pages)

	c = {'ciudades':ciudades,'filtro':filtro,'msg':ciudades.count}
  	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def ciudad_deleteView(request, id = None, template_name='ciudades/ciudades.html'):
	if request.user.has_perm('envios.delete_ciudad'):
		ciudad = get_object_or_404(City, pk=id)
		ciudad.delete()

	return HttpResponseRedirect('/ciudades/')