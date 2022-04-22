from cProfile import label
from datetime import datetime 
from django import forms
from .models import QuizAnswer

class QuizAnswerForm(forms.ModelForm):
    class Meta:
        model = QuizAnswer
        fields = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'name']