# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20170901_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScholarshipType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('scholarship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Scholarship')),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='scholarship_type',
        ),
        migrations.AlterField(
            model_name='member',
            name='scholarship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.ScholarshipType'),
        ),
    ]