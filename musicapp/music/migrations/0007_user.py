# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20150324_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField()),
                ('preference', models.IntegerField(default=1)),
                ('item_id', models.ForeignKey(to='music.Item1')),
                ('user_id', models.ForeignKey(to='music.Login')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
