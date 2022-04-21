from django.urls import path, include
from django.contrib import admin

import homepage.urls as homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(homepage)),
    path('ranking/', include('ranking.urls')),
]
