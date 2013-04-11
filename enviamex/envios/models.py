from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cities_light.models import City

class Cliente(models.Model):
	nombre = models.CharField(max_length=40)
	edad = models.CharField(default='', max_length=3)
	rfc = models.CharField(default='', null=True, blank=True, max_length=13)
	#DIRECCION
	ciudad = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
	codigo_postal = models.CharField(max_length=5)
	#Domicilio
	dir_calle = models.CharField(max_length=100, blank=True, null=True)
	dir_no_exterior = models.CharField(max_length=10, blank=True, null=True)
	dir_no_interior = models.CharField(max_length=10, blank=True, null=True)
	dir_colonia = models.CharField(max_length=100, blank=True, null=True)
	dir_poblacion = models.CharField(max_length=100, blank=True, null=True)
	dir_referencia = models.CharField(max_length=100, blank=True, null=True)
	usuario = models.OneToOneField(User, blank=True, null=True)
	telefono = models.CharField(default='', max_length=10, blank=True, null=True)
	TIPOS = (
		('A', 'Administrador'),
		('C', 'Cliente'),
		)
	tipo = models.CharField(max_length=10, choices=TIPOS, default='C')

	ocupacion = models.CharField(max_length=30, blank=True, null=True)
	
	def __unicode__(self):
		return self.nombre

class Envio(models.Model):
	descripcion 	= models.CharField(max_length=200)
	fecha_salida 	= models.DateTimeField(default=datetime.now())
	fecha_llegada 	= models.DateTimeField(blank=True)
	peso			= models.CharField(max_length=100, blank=True, null=True)
	tamano			= models.CharField(max_length=100, blank=True, null=True)
	
	TIPOS = (
		('N', 'NORMAL'),
		('U', 'URGENTE'),
		('MU', 'MUY URGENTE'),
		)
	tipo = models.CharField(max_length=10, choices=TIPOS, default='N')
	cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)

	def __unicode__(self):
		return self.descripcion