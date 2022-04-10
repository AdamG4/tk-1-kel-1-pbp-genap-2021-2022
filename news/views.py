from django.shortcuts import render

from .models import NewsArticle
from .forms import NewsArticleForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from datetime import datetime

def index(request):
    response = {'articles': NewsArticle.objects.all().values()}

    return render(request, 'news.html', response)

@login_required(login_url="/admin/login")
def post_news_article(request):
    news_article = NewsArticle(author=User.get_username(request.user), date=datetime.now())

    post_form = NewsArticleForm(request.POST , request.FILES, instance=news_article)

    if request.method == "POST":
        if post_form.is_valid():
            post_form.save()

    response = {"post_form" : post_form}

    return render(request, "post_news_article.html", response)