from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.db import models

from .models import Profile
#from .forms import NewsArticleForm
from django.contrib.auth.decorators import login_required

def index(request):
    response = {'profiles': Profile.objects.all().values()}

    print(Profile.objects.all().values())

    return render(request, 'profiles.html', response)

def post_profile(request):
    response = {'profiles': Profile.objects.all().values()}

    return render(request, 'profiles.html', response)