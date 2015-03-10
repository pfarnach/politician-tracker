# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20150310_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='politician',
            name='first_elected',
            field=models.DateField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
