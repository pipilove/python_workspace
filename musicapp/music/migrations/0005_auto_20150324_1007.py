# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20150320_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item1',
            name='item_id',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='login',
            name='user_id',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
    ]
