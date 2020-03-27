# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-01-28 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testrun', '0003_testrunconfigforinstance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testrunconfig',
            name='memory_limit',
            field=models.IntegerField(default=131072, verbose_name='memory limit (KiB)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testrunconfig',
            name='time_limit',
            field=models.IntegerField(default=10000, verbose_name='time limit (ms)'),
            preserve_default=False,
        ),
    ]