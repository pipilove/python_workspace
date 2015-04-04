# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0017_auto_20150326_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='item_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
