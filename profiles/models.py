from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.CharField(default='name', max_length=100)
    content = models.TextField(default='content')
    votes = models.IntegerField(default=0)