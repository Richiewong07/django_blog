# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-07 23:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20180407_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='users',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
