# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-05 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0002_auto_20170904_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorsorder',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
