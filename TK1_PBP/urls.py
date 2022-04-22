from django.urls import path, include
from django.contrib import admin

import homepage.urls as homepage
import news.urls as news
import scoreboard.urls as scoreboard
import profiles.urls as profiles
import forums.urls as forums
import quiz.urls as quiz
import game.urls as game

from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(homepage)),
    path('', include("django.contrib.auth.urls")),

    path("register/", v.register, name="register"),

    path('news/', include(news)),
    path('scoreboard/', include(scoreboard)),
    path('profiles/', include(profiles)),
    path('forums/', include(forums)),
    path('quiz/', include(quiz)),
    path('game/', include(game))
]
