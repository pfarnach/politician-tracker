# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20150310_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='politician',
            name='id_fec',
            field=models.IntegerField(default=None, max_length=500, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='politician',
            name='id_lis',
            field=models.IntegerField(default=None, max_length=500, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='politician',
            name='id_maplight',
            field=models.IntegerField(default=None, max_length=500, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='politician',
            name='id_opensecrets',
            field=models.IntegerField(default=None, max_length=500, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='politician',
            name='id_thomas',
            field=models.IntegerField(default=None, max_length=500, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='politician',
            name='id_votesmart',
            field=models.IntegerField(default=None, max_length=500, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
