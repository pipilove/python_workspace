# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0016_auto_20150326_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hot100',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
            preserve_default=True,
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
