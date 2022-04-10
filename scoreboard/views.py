from django.shortcuts import render

from .models import Score
from .forms import ScoreForm
from django.contrib.auth.decorators import login_required

def index(request):
    response = {'scoreboard': Score.objects.all().values()}

    return render(request, 'scoreboard.html', response)

@login_required(login_url="/admin/login")
def post_score(request):
    post_form = ScoreForm(request.POST , request.FILES)

    if request.method == "POST":
        if post_form.is_valid():
            post_form.save()

    response = {"post_form" : post_form}

    return render(request, "post_score.html", response)