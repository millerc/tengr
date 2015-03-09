# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0008_auto_20140821_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='vimeo_id',
            field=models.CharField(max_length=16, default='91600576'),
            preserve_default=False,
        ),
    ]
