# Generated by Django 4.0.3 on 2022-04-09 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='content',
            field=models.TextField(default='content'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='name', max_length=100),
        ),
    ]
