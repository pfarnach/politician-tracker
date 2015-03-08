# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20150307_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='politician',
            name='rep_district',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='politician',
            name='sen_rank',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
    ]
