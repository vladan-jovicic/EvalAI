# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-15 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_added_new_fields_to_submission_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='completed_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='execution_time_limit',
            field=models.PositiveIntegerField(db_index=True, default=300),
        ),
        migrations.AlterField(
            model_name='submission',
            name='method_description',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='method_name',
            field=models.CharField(db_index=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='project_url',
            field=models.CharField(db_index=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='publication_url',
            field=models.CharField(db_index=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='started_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.CharField(choices=[('submitted', 'submitted'), ('running', 'running'), ('failed', 'failed'), (
                'cancelled', 'cancelled'), ('finished', 'finished'), ('submitting', 'submitting')], db_index=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='submission',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
