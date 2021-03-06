# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-06 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0002_auto_20170706_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventure',
            name='author',
            field=models.CharField(default='Gary Gygax', max_length=100),
        ),
        migrations.AddField(
            model_name='adventure',
            name='publication_year',
            field=models.IntegerField(default=2017),
        ),
        migrations.AlterField(
            model_name='adventure',
            name='system',
            field=models.CharField(choices=[('ADD1E', 'AD&D (1st edition)'), ('ADD2E', 'AD&D (2nd edition)'), ('DD3E', 'D&D (3rd edition)'), ('DD4E', 'D&D (4th edition)'), ('DD5E', 'D&D (5th edition)'), ('DDMV', 'Moldvay D&D'), ('DDMZ', 'Mentzer D&D')], default='DD5E', max_length=100),
        ),
    ]
