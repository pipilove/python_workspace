# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20150320_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_id', models.CharField(max_length=30)),
                ('item_name', models.CharField(max_length=50)),
                ('art_name', models.CharField(max_length=30)),
                ('item_link', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
