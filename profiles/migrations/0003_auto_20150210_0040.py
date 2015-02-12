# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150210_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='chamber',
            field=models.CharField(default=b'n/a', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='district',
            field=models.CharField(default=b'n/a', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='notes',
            field=models.CharField(default=b'n/a', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='party',
            field=models.CharField(default=b'n/a', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='rank',
            field=models.CharField(default=b'n/a', max_length=50),
            preserve_default=True,
        ),
    ]
