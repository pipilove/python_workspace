# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_auto_20150326_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item2',
            name='id',
        ),
        migrations.AlterField(
            model_name='hot100',
            name='item_id',
            field=models.ForeignKey(to='music.Item1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item2',
            name='item_id',
            field=models.AutoField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
