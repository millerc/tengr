# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128)),
                ('population', models.IntegerField()),
                ('logo', models.ImageField(upload_to='')),
                ('marker', models.ImageField(upload_to='')),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('headine', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('community', models.ForeignKey(to='tgr.Community')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterOrderWithRespectTo(
            name='reason',
            order_with_respect_to='community',
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128)),
                ('border', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('content', models.TextField()),
                ('modal', models.TextField(null=True, blank=True)),
                ('reason', models.OneToOneField(to='tgr.Reason')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
    ]
