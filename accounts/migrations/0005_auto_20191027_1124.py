# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-27 11:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191027_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback_new',
            old_name='created_on',
            new_name='created_date',
        ),
    ]