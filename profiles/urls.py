from django.urls import path
from .views import index, post_profile
from django.conf.urls.static import static
from TK1_PBP import settings

urlpatterns = [
    path('', index, name='index'),
    path('post-profile', post_profile, name='post-profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)