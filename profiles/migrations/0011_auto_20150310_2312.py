# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20150310_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='id_fec',
            field=models.CharField(default=None, max_length=500, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='id_lis',
            field=models.CharField(default=None, max_length=500, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='id_opensecrets',
            field=models.CharField(default=None, max_length=500, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='id_thomas',
            field=models.CharField(default=None, max_length=500, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
