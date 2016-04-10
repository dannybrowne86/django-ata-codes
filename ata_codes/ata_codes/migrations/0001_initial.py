# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ATACode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary_ata_code', models.PositiveSmallIntegerField(verbose_name=b'Primary ATA Code')),
                ('secondary_ata_code', models.PositiveSmallIntegerField(verbose_name=b'Secondary ATA Code')),
                ('last_change_date', models.DateField()),
                ('name', models.CharField(max_length=64)),
                ('severity_factor', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ['primary_ata_code', 'secondary_ata_code', 'name'],
                'verbose_name': 'ATA Code',
            },
        ),
        migrations.AlterUniqueTogether(
            name='atacode',
            unique_together=set([('primary_ata_code', 'secondary_ata_code')]),
        ),
    ]
