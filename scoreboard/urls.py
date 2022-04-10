from django.urls import path
from .views import index, post_score

urlpatterns = [
    path('', index, name='index'),
    path('post-score/', post_score, name='post-score'),
]
