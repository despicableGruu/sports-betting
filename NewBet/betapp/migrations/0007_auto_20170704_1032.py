# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('betapp', '0006_appuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='AppUser',
        ),
    ]
