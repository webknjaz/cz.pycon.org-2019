# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-28 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='link',
        ),
        migrations.AddField(
            model_name='announcement',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
