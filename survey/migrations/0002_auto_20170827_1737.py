# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 17:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 27, 17, 37, 59, 124585)),
        ),
        migrations.AlterField(
            model_name='answer',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 27, 17, 37, 59, 124556)),
        ),
        migrations.AlterField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 27, 17, 37, 59, 123444)),
        ),
    ]
