# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Politician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('official_full_name', models.CharField(max_length=50, blank=True)),
                ('birthday', models.CharField(default=None, max_length=50)),
                ('gender', models.CharField(default=None, max_length=50)),
                ('religion', models.CharField(default=None, max_length=50)),
                ('address', models.CharField(default=None, max_length=500)),
                ('office', models.CharField(default=None, max_length=500)),
                ('contact_form', models.URLField(default=None, max_length=500)),
                ('phone', models.CharField(default=None, max_length=50)),
                ('id_bioguide', models.CharField(max_length=50)),
                ('id_govtrack', models.IntegerField(default=None, unique=True, max_length=50, blank=True)),
                ('party', models.CharField(default=None, max_length=50, blank=True)),
                ('state', models.CharField(default=None, max_length=50, blank=True)),
                ('chamber', models.CharField(default=None, max_length=50, blank=True)),
                ('notes', models.CharField(default=None, max_length=50, blank=True)),
                ('url', models.URLField(default=None, max_length=1000, blank=True)),
                ('rss_url', models.URLField(default=None, unique=True, max_length=1000, blank=True)),
                ('term_end', models.DateField(default=None, null=True, blank=True)),
                ('role', models.CharField(default=None, max_length=50, blank=True)),
                ('role_start', models.DateField(default=None, max_length=50, blank=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
