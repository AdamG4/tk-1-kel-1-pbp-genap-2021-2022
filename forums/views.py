from django.shortcuts import render

from .models import ForumPost
from .forms import ForumPostForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from datetime import datetime

def index(request):
    response = {'posts': ForumPost.objects.all().values()}

    return render(request, 'forums.html', response)

@login_required(login_url="/admin/login")
def post_to_forum(request):
    forum_post = ForumPost(author=User.get_username(request.user), date=datetime.now())

    post_form = ForumPostForm(request.POST , request.FILES, instance=forum_post)

    if request.method == "POST":
        if post_form.is_valid():
            post_form.save()

    response = {"post_form" : post_form}

    return render(request, "post_forum_post.html", response)