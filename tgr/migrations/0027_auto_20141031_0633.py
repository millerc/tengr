# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0026_community_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='median_home_value',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='community',
            name='median_household_income',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
