# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-07 22:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='users',
            new_name='user',
        ),
    ]
