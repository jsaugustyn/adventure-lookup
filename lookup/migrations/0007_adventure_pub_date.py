# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-06 18:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0006_adventure_page_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventure',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 6, 18, 3, 40, 666363, tzinfo=utc), verbose_name='date published'),
        ),
    ]
