# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0014_auto_20150326_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hot100',
            name='item_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
