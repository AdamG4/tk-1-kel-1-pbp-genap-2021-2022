from django.urls import path
from .views import index, post_to_forum

urlpatterns = [
    path('', index, name='index'),
    path('post-to-forum', post_to_forum, name='post-to-forum'),
]
