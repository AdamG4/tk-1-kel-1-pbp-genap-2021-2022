from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.CharField(default='name', max_length=100)
    content = models.TextField(default='content')
    image = models.ImageField(upload_to='tk-images')
    votes = models.IntegerField(default=0)