# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='politician',
            old_name='seat',
            new_name='chamber',
        ),
        migrations.RenameField(
            model_name='politician',
            old_name='state',
            new_name='district',
        ),
        migrations.AddField(
            model_name='politician',
            name='notes',
            field=models.CharField(default=datetime.datetime(2015, 2, 10, 0, 37, 9, 893597, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='politician',
            name='rank',
            field=models.CharField(default=datetime.datetime(2015, 2, 10, 0, 37, 40, 285404, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='politician',
            name='name',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
