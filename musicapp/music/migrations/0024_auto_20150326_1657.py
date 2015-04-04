# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0023_auto_20150326_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotmusic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=50, null=True)),
                ('art_name', models.CharField(max_length=30, null=True)),
                ('item_link', models.URLField(null=True)),
                ('item_id', models.ForeignKey(to='music.Item1')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='hot',
            name='item_id',
        ),
        migrations.DeleteModel(
            name='Hot',
        ),
    ]
