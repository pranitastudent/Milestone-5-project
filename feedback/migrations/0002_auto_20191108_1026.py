# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-08 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='user_feedback',
            field=models.TextField(help_text='Please enter your feedback', null=True),
        ),
    ]
