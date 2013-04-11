from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cities_light.models import City

class PerfilUsario(models.Model):
	nombre = models.CharField(max_length=40)
	usuario = models.OneToOneField(User, blank=True, null=True)
	telefono = models.CharField(default='', max_length=10, blank=True, null=True)
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
	fecha_llegada 	= models.DateTimeField(blank=True, null=True)
	peso			= models.CharField(max_length=100, blank=True, null=True)
	tamano			= models.CharField(max_length=100, blank=True, null=True)

	ESTADOS = (
		('E', 'ENTREGADO'),
		('PE', 'POR ENTREGAR'),
		('I', 'INDEFINIDO'),
		)
	estado = models.CharField(max_length=10, choices=ESTADOS, default='PE')

	usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

	def __unicode__(self):
		return self.descripcion