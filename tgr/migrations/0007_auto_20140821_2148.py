# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tgr.models


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0006_reason_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='image',
            field=models.ImageField(upload_to=tgr.models.get_sponsor_image_upload_path, default='31502161.jpg'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='content',
        ),
    ]
