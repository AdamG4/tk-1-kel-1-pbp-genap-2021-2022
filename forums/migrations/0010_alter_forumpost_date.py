# Generated by Django 4.0.3 on 2022-04-09 18:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0009_alter_forumpost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 1, 59, 7, 650392)),
        ),
    ]