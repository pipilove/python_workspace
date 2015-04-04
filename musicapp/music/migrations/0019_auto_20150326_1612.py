# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0018_auto_20150326_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField()),
                ('preference', models.IntegerField(default=1)),
                ('item_id', models.ForeignKey(to='music.Item1')),
                ('user_id', models.ForeignKey(to='music.Login')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='item2tag',
            name='item_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
