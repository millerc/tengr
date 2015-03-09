# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgr', '0012_community_publish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=75)),
                ('notify', models.BooleanField()),
                ('message', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('community', models.ForeignKey(to='tgr.Community')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
