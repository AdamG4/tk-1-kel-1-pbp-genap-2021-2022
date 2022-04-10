from django.db import models
from datetime import datetime

class ForumPost(models.Model):
    title = models.CharField(default="title", max_length=100)
    author = models.CharField(default="author", max_length=100)
    date = models.DateTimeField(default=datetime.now())
    content = models.TextField(default="content")

    reply = models.CharField(default="-", max_length=100)