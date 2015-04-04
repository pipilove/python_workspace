# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0025_auto_20150326_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='item_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
