# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0002_auto_20170831_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingdata',
            name='duo',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='ratingdata',
            name='solo',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='ratingdata',
            name='squad',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
