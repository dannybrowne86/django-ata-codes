# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ATACode'
        db.create_table(u'ata_codes_atacode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('primary_ata_code', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('secondary_ata_code', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('last_change_date', self.gf('django.db.models.fields.DateField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('severity_factor', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'ata_codes', ['ATACode'])

        # Adding unique constraint on 'ATACode', fields ['primary_ata_code', 'secondary_ata_code']
        db.create_unique(u'ata_codes_atacode', ['primary_ata_code', 'secondary_ata_code'])


    def backwards(self, orm):
        # Removing unique constraint on 'ATACode', fields ['primary_ata_code', 'secondary_ata_code']
        db.delete_unique(u'ata_codes_atacode', ['primary_ata_code', 'secondary_ata_code'])

        # Deleting model 'ATACode'
        db.delete_table(u'ata_codes_atacode')


    models = {
        u'ata_codes.atacode': {
            'Meta': {'unique_together': "(('primary_ata_code', 'secondary_ata_code'),)", 'object_name': 'ATACode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_change_date': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'primary_ata_code': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'secondary_ata_code': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'severity_factor': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['ata_codes']