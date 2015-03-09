# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census_places', '__first__'),
        ('tgr', '0025_community_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='place',
            field=models.OneToOneField(null=True, to='census_places.PlaceBoundary', blank=True),
            preserve_default=True,
        ),
    ]
