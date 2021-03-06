# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-26 01:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0022_auto_20160420_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='postevent',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='postevent',
            name='lng',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='postevent',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 26, 1, 17, 59, 237423, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postevent',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 26, 1, 17, 59, 237393, tzinfo=utc)),
        ),
    ]
