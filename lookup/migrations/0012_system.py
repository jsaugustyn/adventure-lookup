# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-07 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0011_auto_20170706_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_name', models.CharField(max_length=150)),
            ],
        ),
    ]