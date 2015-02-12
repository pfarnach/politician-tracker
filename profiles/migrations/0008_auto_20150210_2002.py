# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20150210_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='wiki_url',
            field=models.URLField(default=None, max_length=1000, blank=True),
            preserve_default=True,
        ),
    ]
