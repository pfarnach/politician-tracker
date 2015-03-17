# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_cachedopensecrets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cachedopensecrets',
            name='top_contributor',
            field=jsonfield.fields.JSONField(default=None, max_length=5000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cachedopensecrets',
            name='top_industry',
            field=jsonfield.fields.JSONField(default=None, max_length=5000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
