# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20150325_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hot100',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_id', models.ForeignKey(to='music.Item1')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
