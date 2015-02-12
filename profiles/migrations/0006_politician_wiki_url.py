# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20150210_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='politician',
            name='wiki_url',
            field=models.URLField(default=1000, blank=True),
            preserve_default=True,
        ),
    ]
