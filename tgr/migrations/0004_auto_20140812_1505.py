# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0003_community_region'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reason',
            old_name='headine',
            new_name='headline',
        ),
    ]
