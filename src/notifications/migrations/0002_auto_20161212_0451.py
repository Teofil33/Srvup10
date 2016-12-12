# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='action_object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='target_object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
