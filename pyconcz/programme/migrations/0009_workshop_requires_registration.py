# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-22 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0008_auto_20180519_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='requires_registration',
            field=models.BooleanField(default=True),
        ),
    ]
