# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-06 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adventure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adv_title', models.CharField(max_length=200)),
                ('adv_desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comments', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='submitted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup.User'),
        ),
        migrations.AddField(
            model_name='adventure',
            name='ratings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup.Rating'),
        ),
        migrations.AddField(
            model_name='adventure',
            name='submitted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup.User'),
        ),
    ]
