# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_politician_profile_pic_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='profile_pic_url',
            field=models.URLField(default=1000, blank=True),
            preserve_default=True,
        ),
    ]
