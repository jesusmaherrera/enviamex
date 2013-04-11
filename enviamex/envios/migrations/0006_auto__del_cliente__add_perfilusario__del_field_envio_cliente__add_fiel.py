# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Cliente'
        db.delete_table('envios_cliente')

        # Adding model 'PerfilUsario'
        db.create_table('envios_perfilusario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('usuario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(default='', max_length=10, null=True, blank=True)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.City'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('dir_calle', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('dir_no_exterior', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('dir_no_interior', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('dir_colonia', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('dir_poblacion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('dir_referencia', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(default='C', max_length=10)),
            ('ocupacion', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
        ))
        db.send_create_signal('envios', ['PerfilUsario'])

        # Deleting field 'Envio.cliente'
        db.delete_column('envios_envio', 'cliente_id')

        # Adding field 'Envio.usuario'
        db.add_column('envios_envio', 'usuario',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['envios.PerfilUsario'], null=True, on_delete=models.SET_NULL, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Cliente'
        db.create_table('envios_cliente', (
            ('edad', self.gf('django.db.models.fields.CharField')(default='', max_length=3)),
            ('dir_calle', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(default='C', max_length=10)),
            ('dir_no_interior', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('dir_no_exterior', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(default='', max_length=10, null=True, blank=True)),
            ('rfc', self.gf('django.db.models.fields.CharField')(default='', max_length=13, null=True, blank=True)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.City'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('dir_poblacion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('ocupacion', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('dir_colonia', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dir_referencia', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('envios', ['Cliente'])

        # Deleting model 'PerfilUsario'
        db.delete_table('envios_perfilusario')

        # Adding field 'Envio.cliente'
        db.add_column('envios_envio', 'cliente',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['envios.Cliente'], null=True, on_delete=models.SET_NULL, blank=True),
                      keep_default=False)

        # Deleting field 'Envio.usuario'
        db.delete_column('envios_envio', 'usuario_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cities_light.city': {
            'Meta': {'unique_together': "(('region', 'name'),)", 'object_name': 'City'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.Region']", 'null': 'True', 'blank': 'True'}),
            'search_names': ('cities_light.models.ToSearchTextField', [], {'default': "''", 'max_length': '4000', 'db_index': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        'cities_light.country': {
            'Meta': {'object_name': 'Country'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'code2': ('django.db.models.fields.CharField', [], {'max_length': '2', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'code3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"}),
            'tld': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'blank': 'True'})
        },
        'cities_light.region': {
            'Meta': {'unique_together': "(('country', 'name'),)", 'object_name': 'Region'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'geoname_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'envios.envio': {
            'Meta': {'object_name': 'Envio'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fecha_llegada': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'fecha_salida': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 11, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'peso': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tamano': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '10'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['envios.PerfilUsario']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        },
        'envios.perfilusario': {
            'Meta': {'object_name': 'PerfilUsario'},
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.City']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'dir_calle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'dir_colonia': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'dir_no_exterior': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'dir_no_interior': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'dir_poblacion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'dir_referencia': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'ocupacion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '10'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['envios']