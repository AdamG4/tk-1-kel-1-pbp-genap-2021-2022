# Generated by Django 4.0.3 on 2022-04-09 03:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_newsarticle_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 9, 10, 56, 9, 26169)),
        ),
    ]