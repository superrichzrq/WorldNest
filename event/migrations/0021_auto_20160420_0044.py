# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 00:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0020_auto_20160419_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='religion',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='postevent',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 20, 0, 44, 55, 376782, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postevent',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 20, 0, 44, 55, 376751, tzinfo=utc)),
        ),
    ]
