from django.urls import path
from .views import index, post_news_article

urlpatterns = [
    path('', index, name='index'),
    path('post-news-article/', post_news_article, name='post-news-article'),
]
