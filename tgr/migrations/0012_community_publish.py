# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0011_auto_20140909_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='publish',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
