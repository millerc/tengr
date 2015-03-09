# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0018_auto_20140918_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='video_id',
            field=models.CharField(max_length=16, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='community',
            unique_together=set([('name', 'region')]),
        ),
    ]
