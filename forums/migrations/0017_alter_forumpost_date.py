# Generated by Django 4.0.2 on 2022-04-22 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0016_alter_forumpost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 22, 19, 58, 45, 834642)),
        ),
    ]
