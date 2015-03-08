# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='birthday',
            field=models.CharField(default=None, max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='chamber',
            field=models.CharField(default=None, max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='contact_form',
            field=models.URLField(default=None, max_length=5000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='first_name',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='gender',
            field=models.CharField(default=None, max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='id_bioguide',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='id_govtrack',
            field=models.IntegerField(default=None, unique=True, max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='last_name',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='notes',
            field=models.CharField(default=None, max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='official_full_name',
            field=models.CharField(max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='party',
            field=models.CharField(default=None, max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='phone',
            field=models.CharField(default=None, max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='religion',
            field=models.CharField(default=None, max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='role',
            field=models.CharField(default=None, max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='role_start',
            field=models.DateField(default=None, max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='state',
            field=models.CharField(default=None, max_length=500, blank=True),
            preserve_default=True,
        ),
    ]
