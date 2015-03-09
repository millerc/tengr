# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0022_attribute_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='name',
            field=models.CharField(unique=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='slug',
            field=models.SlugField(unique=True, max_length=64),
        ),
    ]
