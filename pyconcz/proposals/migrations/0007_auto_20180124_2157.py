# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-24 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0006_auto_20180124_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='referral_link',
            field=models.URLField(blank=True, default='', help_text='If you have a recording of you giving a talk or leading a workshop, you can paste the link here.', verbose_name='Got a video?'),
        ),
    ]
