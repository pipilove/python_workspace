# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item1',
            name='id',
        ),
        migrations.RemoveField(
            model_name='login',
            name='id',
        ),
        migrations.AlterField(
            model_name='item1',
            name='item_id',
            field=models.AutoField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item1',
            name='item_link',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='login',
            name='user_id',
            field=models.AutoField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='login',
            name='user_name',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
    ]
