# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-26 10:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191023_1422'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feedback',
            new_name='feedback_new',
        ),
    ]
