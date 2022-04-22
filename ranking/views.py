from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import FootballPlayer
# Create your views here.
def index(request):
    player = FootballPlayer.objects.all().values()
    template = loader.get_template('rankHome.html')
    context = {
        'player': player
    }
    return HttpResponse(template.render(context, request))