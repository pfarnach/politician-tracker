# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20150210_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='politician',
            name='profile_pic_url',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
