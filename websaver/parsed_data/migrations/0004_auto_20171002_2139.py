# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0003_auto_20170831_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingdata',
            name='duofpp',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='ratingdata',
            name='solofpp',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='ratingdata',
            name='squadfpp',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
