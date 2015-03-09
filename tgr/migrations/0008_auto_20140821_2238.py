# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tgr.models


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0007_auto_20140821_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='title_image',
            field=models.ImageField(upload_to=tgr.models.get_community_title_upload_path, default='31502161.jpg'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='community',
            name='logo',
        ),
    ]
