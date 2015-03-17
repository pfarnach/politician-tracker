# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_usersubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='CachedOpenSecrets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('top_contributor', models.CharField(default=None, max_length=5000, null=True, blank=True)),
                ('top_industry', models.CharField(default=None, max_length=5000, null=True, blank=True)),
                ('net_low', models.IntegerField(default=None, max_length=50)),
                ('net_high', models.IntegerField(default=None, max_length=50)),
                ('politician', models.ForeignKey(to='profiles.Politician')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
