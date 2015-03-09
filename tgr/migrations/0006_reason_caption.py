# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0005_auto_20140816_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='reason',
            name='caption',
            field=models.TextField(default="I'm a caption"),
            preserve_default=False,
        ),
    ]
