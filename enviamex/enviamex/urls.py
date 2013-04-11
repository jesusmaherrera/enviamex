from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^login/$', 'envios.views.ingresar'),
    url(r'^logout/$', 'envios.views.logoutUser'),

    url(r'^$', 'envios.views.index', name='index'),
    url(r'^envios/$', 'envios.views.envios_View', name='envios'),
    url(r'^clientes/$', 'envios.views.clientes_View', name='clientes'),
    (r'^cliente/$', 'envios.views.cliente_manageView'),
    (r'^cliente/(?P<id>\d+)', 'envios.views.cliente_manageView'),

    (r'^clienteN/$', 'envios.views.clientenormal_manageView'),
    (r'^clienteN/(?P<id>\d+)', 'envios.views.clientenormal_manageView'),
    

    (r'^cliente/delete/(?P<id>\d+)/', 'envios.views.cliente_deleteView'),

    (r'^envio/$', 'envios.views.envio_manageView'),
    (r'^envio/(?P<id>\d+)', 'envios.views.envio_manageView'),
    # url(r'^enviamex/', include('enviamex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()