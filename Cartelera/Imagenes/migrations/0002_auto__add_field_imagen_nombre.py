# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Imagen.nombre'
        db.add_column(u'Imagenes_imagen', 'nombre',
                      self.gf('django.db.models.fields.CharField')(default=3, max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Imagen.nombre'
        db.delete_column(u'Imagenes_imagen', 'nombre')


    models = {
        u'Geolocalizacion.geolocalizacion': {
            'Meta': {'object_name': 'Geolocalizacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'Imagenes.imagen': {
            'Meta': {'object_name': 'Imagen'},
            'geo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Geolocalizacion.Geolocalizacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['Imagenes']