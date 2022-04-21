from django.db import models

# Create your models here.
class FootballPlayer(models.Model):
    fullname = models.CharField(max_length=30)
    age = models.IntegerField()
    league = models.CharField(max_length=30)
    nationality = models.CharField(max_length=20)