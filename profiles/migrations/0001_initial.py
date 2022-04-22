# Generated by Django 4.0.3 on 2022-04-22 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=100)),
                ('content', models.TextField(default='content')),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
    ]
