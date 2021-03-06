# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 22:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0015_auto_20160418_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='postevent',
            name='event_page',
            field=models.CharField(default=b'', max_length=500),
        ),
        migrations.AddField(
            model_name='usersetting',
            name='business',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usersetting',
            name='charity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usersetting',
            name='culture',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usersetting',
            name='education',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usersetting',
            name='entertainment',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usersetting',
            name='fashion',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usersetting',
            name='food',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usersetting',
            name='health',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usersetting',
            name='hobbies',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usersetting',
            name='holiday',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usersetting',
            name='lifestyle',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usersetting',
            name='music',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usersetting',
            name='performing',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usersetting',
            name='politics',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usersetting',
            name='sports',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usersetting',
            name='technology',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usersetting',
            name='travel',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='postevent',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 18, 22, 42, 32, 587260, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postevent',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 18, 22, 42, 32, 587228, tzinfo=utc)),
        ),
    ]
