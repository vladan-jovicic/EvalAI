# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-03 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0017_added_leaderboard_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengePhaseSplit',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('visibility', models.CharField(
                    choices=[(
                        '1', 'host'), ('2', 'owner and host'), ('3', 'public')], default='3', max_length=1)),
                ('challenge_phase', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='challenges.ChallengePhase')),
                ('dataset_split', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='challenges.DatasetSplit')),
                ('leaderboard', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='challenges.Leaderboard')),
            ],
            options={
                'db_table': 'challenge_phase_split',
            },
        ),
    ]
