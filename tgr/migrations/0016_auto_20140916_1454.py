# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tgr.models
import localflavor.us.models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0015_auto_20140916_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('phone', localflavor.us.models.PhoneNumberField(max_length=20)),
                ('website', models.URLField()),
                ('image', models.ImageField(upload_to=tgr.models.get_attraction_image_upload_path, null=True, blank=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('region', models.ForeignKey(to='tgr.Region')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='attractions',
            name='region',
        ),
        migrations.DeleteModel(
            name='Attractions',
        ),
    ]
