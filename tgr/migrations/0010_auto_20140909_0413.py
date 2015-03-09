# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tgr.models


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0009_community_vimeo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='title_image',
            field=models.ImageField(null=True, blank=True, upload_to=tgr.models.get_community_title_upload_path),
        ),
        migrations.AlterField(
            model_name='community',
            name='vimeo_id',
            field=models.CharField(null=True, blank=True, max_length=16),
        ),
    ]
