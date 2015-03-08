# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20150307_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='notes',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
    ]
