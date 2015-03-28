# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Geolocalizacion'
        db.create_table(u'Geolocalizacion_geolocalizacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('latitud', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('longitud', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'Geolocalizacion', ['Geolocalizacion'])


    def backwards(self, orm):
        # Deleting model 'Geolocalizacion'
        db.delete_table(u'Geolocalizacion_geolocalizacion')


    models = {
        u'Geolocalizacion.geolocalizacion': {
            'Meta': {'object_name': 'Geolocalizacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['Geolocalizacion']