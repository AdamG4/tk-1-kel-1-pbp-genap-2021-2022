from django.shortcuts import render

from .models import QuizAnswer
from .forms import QuizAnswerForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'quiz.html')
    
@login_required(login_url="/admin/login")
def take(request):
    post_form = QuizAnswerForm(request.POST , request.FILES)

    if request.method == "POST":
        if post_form.is_valid():
            post_form.save()

    response = {"post_form" : post_form}

    return render(request, "take_quiz.html", response)

def results(request):
    answers = QuizAnswer.objects.all().values()

    response = {'answers': answers}

    return render(request, 'results_quiz.html', response)