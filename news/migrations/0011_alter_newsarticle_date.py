# Generated by Django 4.0.3 on 2022-04-09 04:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_alter_newsarticle_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 9, 11, 12, 44, 973073)),
        ),
    ]
