# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0002_auto_20140812_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='region',
            field=models.ForeignKey(to='tgr.Region', default=1),
            preserve_default=False,
        ),
    ]
