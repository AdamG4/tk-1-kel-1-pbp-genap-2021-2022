from django.db import models
from datetime import datetime 

class Score(models.Model):
    team_1 = models.CharField(default="team1", max_length=100)
    score_1 = models.PositiveIntegerField(default=0)

    team_2 = models.CharField(default="team2", max_length=100)
    score_2 = models.PositiveIntegerField(default=0)

    date = models.DateTimeField(default=datetime.now())