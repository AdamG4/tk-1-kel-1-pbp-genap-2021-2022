# Generated by Django 4.0.3 on 2022-04-08 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 8, 20, 53, 57, 987840)),
        ),
    ]