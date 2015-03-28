# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Portada.geolocalizacion'
        db.add_column(u'Portadas_portada', 'geolocalizacion',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['Geolocalizacion.Geolocalizacion']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Portada.geolocalizacion'
        db.delete_column(u'Portadas_portada', 'geolocalizacion_id')


    models = {
        u'Ambitos.ambito': {
            'Meta': {'object_name': 'Ambito'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'Geolocalizacion.geolocalizacion': {
            'Meta': {'object_name': 'Geolocalizacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'Portadas.portada': {
            'Meta': {'object_name': 'Portada'},
            'ambito': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Ambitos.Ambito']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '260'}),
            'geolocalizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Geolocalizacion.Geolocalizacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resumen': ('django.db.models.fields.TextField', [], {'max_length': '140'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['Portadas']