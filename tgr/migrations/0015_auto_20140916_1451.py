# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models
import django.contrib.gis.db.models.fields
import tgr.models


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0014_auto_20140912_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attractions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('phone', localflavor.us.models.PhoneNumberField(max_length=20)),
                ('website', models.URLField()),
                ('image', models.ImageField(null=True, blank=True, upload_to=tgr.models.get_attraction_image_upload_path)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('region', models.ForeignKey(to='tgr.Region')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name_plural': 'Feedback'},
        ),
    ]
