# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_auto_20150317_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cachedopensecrets',
            name='net_high',
            field=models.IntegerField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cachedopensecrets',
            name='net_low',
            field=models.IntegerField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
