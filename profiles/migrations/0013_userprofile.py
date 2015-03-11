# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0012_politician_first_elected'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zipcode', models.IntegerField(default=None, max_length=50)),
                ('last_login', models.DateTimeField(default=None, null=True, blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('email_pref', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('avatar', models.CharField(default=None, max_length=1000, unique=True, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
