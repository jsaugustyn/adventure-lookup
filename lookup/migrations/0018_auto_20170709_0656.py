# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-09 10:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0017_auto_20170709_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adventure',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
    ]
