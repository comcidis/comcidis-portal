# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0005_publication_bibtex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='resume',
            field=models.TextField(blank=True),
        ),
    ]
