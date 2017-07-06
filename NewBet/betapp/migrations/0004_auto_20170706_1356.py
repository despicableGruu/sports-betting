# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betapp', '0003_auto_20170706_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='bet_result',
            field=models.IntegerField(blank=True, choices=[(0, 'LOST'), (1, 'WIN')], default=0),
        ),
    ]
