# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0024_auto_20150326_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotmusic',
            name='item_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
