# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-25 10:34
from __future__ import unicode_literals

import base.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_squashed_0005_upload_unique_random_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='input_file',
            field=models.FileField(
                upload_to=base.utils.RandomFileName(
                    'submission_files/submission_{id}')),
        ),
        migrations.AlterField(
            model_name='submission',
            name='stderr_file',
            field=models.FileField(
                blank=True, null=True, upload_to=base.utils.RandomFileName(
                    'submission_files/submission_{id}')),
        ),
        migrations.AlterField(
            model_name='submission',
            name='stdout_file',
            field=models.FileField(
                blank=True, null=True, upload_to=base.utils.RandomFileName(
                    'submission_files/submission_{id}')),
        ),
    ]
