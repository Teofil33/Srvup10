# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='video',
            unique_together=set([('slug', 'category')]),
        ),
    ]