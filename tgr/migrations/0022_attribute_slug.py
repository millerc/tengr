# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0021_auto_20141004_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='slug',
            field=models.SlugField(default='slug', max_length=64),
            preserve_default=False,
        ),
    ]
