# Generated by Django 4.0.3 on 2022-04-22 08:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0016_alter_score_date_alter_score_score_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 22, 15, 5, 7, 666238)),
        ),
    ]
