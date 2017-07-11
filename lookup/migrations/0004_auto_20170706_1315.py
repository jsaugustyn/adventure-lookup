# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-06 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0003_auto_20170706_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventure',
            name='source',
            field=models.CharField(default='Dungeon Magazine, November/December 1986, Issue 2', max_length=200),
        ),
        migrations.AddField(
            model_name='adventure',
            name='source_url',
            field=models.URLField(default='', max_length=500),
        ),
    ]