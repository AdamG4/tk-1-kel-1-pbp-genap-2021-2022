# Generated by Django 4.0.3 on 2022-04-22 14:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_1', models.CharField(default='team1', max_length=100)),
                ('score_1', models.PositiveIntegerField(default=0)),
                ('team_2', models.CharField(default='team2', max_length=100)),
                ('score_2', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 4, 22, 21, 30, 1, 971628))),
            ],
        ),
    ]
