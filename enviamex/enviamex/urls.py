from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import autocomplete_light
autocomplete_light.autodiscover()
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^login/$', 'envios.views.ingresar'),
    url(r'^logout/$', 'envios.views.logoutUser'),

    url(r'^$', 'envios.views.index', name='index'),
    url(r'^envios/$', 'envios.views.envios_View', name='envios'),
    (r'^envio/$', 'envios.views.envio_manageView'),
    (r'^envio/(?P<id>\d+)', 'envios.views.envio_manageView'),
    (r'^envio/delete/(?P<id>\d+)/', 'envios.views.envio_deleteView'),

    url(r'^clientes/$', 'envios.views.clientes_View', name='clientes'),
    (r'^usuario/$', 'envios.views.usuario_manageView'),
    (r'^usuario/(?P<id>\d+)', 'envios.views.usuario_manageView'),
    (r'^usuario/delete/(?P<id>\d+)/', 'envios.views.usuario_deleteView'),

    (r'^cliente/$', 'envios.views.cliente_manageView'),
    (r'^cliente/(?P<id>\d+)', 'envios.views.cliente_manageView'),
    url(r'autocomplete/', include('autocomplete_light.urls')),
    
     #Ciudades
    (r'^ciudades/$', 'envios.views.ciudades_View'),
    (r'^ciudad/$', 'envios.views.ciudad_manageView'),
    (r'^ciudad/(?P<id>\d+)/', 'envios.views.ciudad_manageView'),
    (r'^ciudad/delete/(?P<id>\d+)/', 'envios.views.ciudad_deleteView'),

    (r'^contacto/$', 'envios.views.contactoView'),
    (r'^servicios/$', 'envios.views.serviciosView'),
    (r'^recepcion/$', 'envios.views.recepcionView'),
    (r'^dinero/$', 'envios.views.dineroView'),
    
    # url(r'^enviamex/', include('enviamex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()