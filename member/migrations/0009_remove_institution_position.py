# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 00:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_auto_20170902_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='position',
        ),
    ]
