# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0019_auto_20150320_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.CharField(default=None, max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
    ]
