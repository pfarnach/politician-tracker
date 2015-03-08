# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150306_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='slug',
            field=models.SlugField(unique=True, max_length=500),
            preserve_default=True,
        ),
    ]
