# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0020_auto_20141004_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='attributes',
            field=models.ManyToManyField(to='tgr.Attribute', blank=True),
        ),
    ]
