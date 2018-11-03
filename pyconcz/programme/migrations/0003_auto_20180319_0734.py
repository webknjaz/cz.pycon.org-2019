# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-19 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0002_auto_20180319_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='is_backup',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='workshop',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='workshop',
            name='private_note',
            field=models.TextField(blank=True, default='', help_text='DO NOT SHOW ON WEBSITE'),
        ),
    ]
