# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_auto_20150319_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(max_length=500),
            preserve_default=True,
        ),
    ]
