# Generated by Django 4.0.3 on 2022-04-22 13:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0018_alter_forumpost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 22, 20, 54, 27, 608021)),
        ),
    ]
