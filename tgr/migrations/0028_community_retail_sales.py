# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0027_auto_20141031_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='retail_sales',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
