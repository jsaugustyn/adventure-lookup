# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-09 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0018_auto_20170709_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adventure',
            name='submitted_by',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='lookup.User'),
        ),
    ]
