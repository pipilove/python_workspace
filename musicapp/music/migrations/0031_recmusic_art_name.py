# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0030_recmusic_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='recmusic',
            name='art_name',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
    ]
