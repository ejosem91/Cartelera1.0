# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Geolocalizacion.latitud'
        db.alter_column(u'Geolocalizacion_geolocalizacion', 'latitud', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=7))

        # Changing field 'Geolocalizacion.longitud'
        db.alter_column(u'Geolocalizacion_geolocalizacion', 'longitud', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=7))

    def backwards(self, orm):

        # Changing field 'Geolocalizacion.latitud'
        db.alter_column(u'Geolocalizacion_geolocalizacion', 'latitud', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2))

        # Changing field 'Geolocalizacion.longitud'
        db.alter_column(u'Geolocalizacion_geolocalizacion', 'longitud', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2))

    models = {
        u'Geolocalizacion.geolocalizacion': {
            'Meta': {'object_name': 'Geolocalizacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['Geolocalizacion']