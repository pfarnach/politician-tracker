# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20150307_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='address',
            field=models.CharField(default=None, max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='birthday',
            field=models.CharField(default=None, max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='contact_form',
            field=models.URLField(default=None, max_length=5000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='gender',
            field=models.CharField(default=None, max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='id_govtrack',
            field=models.IntegerField(default=None, max_length=500, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='office',
            field=models.CharField(default=None, max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='phone',
            field=models.CharField(default=None, max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='religion',
            field=models.CharField(default=None, max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='role',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='role_start',
            field=models.DateField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='rss_url',
            field=models.URLField(default=None, max_length=1000, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
