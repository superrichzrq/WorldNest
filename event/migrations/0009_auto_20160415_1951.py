# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-15 19:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20160415_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postevent',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 15, 19, 51, 9, 556487, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postevent',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 15, 19, 51, 9, 556454, tzinfo=utc)),
        ),
    ]
