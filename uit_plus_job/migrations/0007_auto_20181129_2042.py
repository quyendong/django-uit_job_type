# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-29 20:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uit_plus_job', '0006_auto_20181129_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='uitplusjob',
            name='max_cleanup_time',
            field=models.DurationField(default=datetime.timedelta(0, 3600)),
        ),
        migrations.AlterField(
            model_name='uitplusjob',
            name='_remote_workspace_id',
            field=models.CharField(default='8ebafcbd-1f16-41f1-a758-96933bc6ccf5', max_length=64),
        ),
    ]
