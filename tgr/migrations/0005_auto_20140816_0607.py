# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tgr.models


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0004_auto_20140812_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='logo',
            field=models.ImageField(upload_to=tgr.models.get_community_logo_upload_path),
        ),
        migrations.AlterField(
            model_name='community',
            name='marker',
            field=models.ImageField(upload_to=tgr.models.get_community_marker_upload_path),
        ),
        migrations.AlterField(
            model_name='reason',
            name='image',
            field=models.ImageField(upload_to=tgr.models.get_reason_image_upload_path),
        ),
    ]
