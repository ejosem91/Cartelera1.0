# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Portada'
        db.create_table(u'Portadas_portada', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('resumen', self.gf('django.db.models.fields.TextField')(max_length=140)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=260)),
        ))
        db.send_create_signal(u'Portadas', ['Portada'])


    def backwards(self, orm):
        # Deleting model 'Portada'
        db.delete_table(u'Portadas_portada')


    models = {
        u'Portadas.portada': {
            'Meta': {'object_name': 'Portada'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '260'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resumen': ('django.db.models.fields.TextField', [], {'max_length': '140'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['Portadas']