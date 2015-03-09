# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0024_auto_20141006_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='color',
            field=colorfield.fields.ColorField(max_length=10, default=0),
            preserve_default=False,
        ),
    ]
