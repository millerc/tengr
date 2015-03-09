# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0023_auto_20141006_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='slug',
            field=models.SlugField(max_length=64),
        ),
    ]
