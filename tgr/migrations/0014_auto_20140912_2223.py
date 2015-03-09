# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0013_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='notify',
            field=models.BooleanField(default=False),
        ),
    ]
