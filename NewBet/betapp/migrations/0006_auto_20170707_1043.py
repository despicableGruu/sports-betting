# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-07 10:43
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betapp', '0005_auto_20170707_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='cash',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
