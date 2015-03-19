# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0017_auto_20150318_0656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(null=True)),
                ('title', models.CharField(max_length=500)),
                ('url', models.URLField(max_length=1000)),
                ('tags', jsonfield.fields.JSONField(default=None, max_length=500, null=True, blank=True)),
                ('politician', models.ForeignKey(to='profiles.Politician')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(default=None)),
                ('vote', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('article', models.ForeignKey(to='profiles.Article')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='cachedopensecrets',
            name='timestamp',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_on',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usersubscription',
            name='timestamp',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
