# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_politician_wiki_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='profile_pic_url',
            field=models.URLField(max_length=1000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='wiki_url',
            field=models.URLField(max_length=1000, blank=True),
            preserve_default=True,
        ),
    ]
