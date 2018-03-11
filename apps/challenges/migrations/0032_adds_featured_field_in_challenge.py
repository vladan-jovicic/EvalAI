# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-29 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0031_add_db_index_to_challenge_related_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='featured',
            field=models.BooleanField(
                db_index=True, default=False, verbose_name='Featured'),
        ),
    ]
