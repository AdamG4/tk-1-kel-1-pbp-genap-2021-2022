from django.db import models
from datetime import datetime

class NewsArticle(models.Model):
    title = models.CharField(default="title", max_length=100)
    author = models.CharField(default="author", max_length=100)
    date = models.DateTimeField(default=datetime.now())
    content = models.TextField(default="content")