# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0020_auto_20150326_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hot100',
            name='item_id',
        ),
        migrations.AlterField(
            model_name='hot100',
            name='id',
            field=models.AutoField(default=0, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
