# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Celebrity'
        db.create_table('celebrity_celebrity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('flagged', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('whitelisted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('celebrity', ['Celebrity'])


    def backwards(self, orm):
        # Deleting model 'Celebrity'
        db.delete_table('celebrity_celebrity')


    models = {
        'celebrity.celebrity': {
            'Meta': {'object_name': 'Celebrity'},
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'whitelisted': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['celebrity']