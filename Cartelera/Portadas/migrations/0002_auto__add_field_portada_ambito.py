# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Portada.ambito'
        db.add_column(u'Portadas_portada', 'ambito',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['Ambitos.Ambito']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Portada.ambito'
        db.delete_column(u'Portadas_portada', 'ambito_id')


    models = {
        u'Ambitos.ambito': {
            'Meta': {'object_name': 'Ambito'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'Portadas.portada': {
            'Meta': {'object_name': 'Portada'},
            'ambito': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Ambitos.Ambito']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '260'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resumen': ('django.db.models.fields.TextField', [], {'max_length': '140'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['Portadas']