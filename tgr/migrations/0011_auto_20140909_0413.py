# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0010_auto_20140909_0413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='community',
            old_name='vimeo_id',
            new_name='video_id',
        ),
    ]
