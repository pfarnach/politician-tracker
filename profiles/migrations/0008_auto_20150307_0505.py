# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20150307_0502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='politician',
            old_name='sen_rank',
            new_name='sen_class',
        ),
    ]
