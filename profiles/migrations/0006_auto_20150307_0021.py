# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20150307_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='rss_url',
            field=models.URLField(default=None, max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
