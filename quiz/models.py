from django.db import models

class QuizAnswer(models.Model):
    mul_choices = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')]

    q0 = models.CharField(choices=mul_choices, max_length=1)
    q1 = models.CharField(choices=mul_choices, max_length=1)
    q2 = models.CharField(choices=mul_choices, max_length=1)
    q3 = models.CharField(choices=mul_choices, max_length=1)
    q4 = models.CharField(choices=mul_choices, max_length=1)
    q5 = models.CharField(choices=mul_choices, max_length=1)
    q6 = models.CharField(choices=mul_choices, max_length=1)
    q7 = models.CharField(choices=mul_choices, max_length=1)
    q8 = models.CharField(choices=mul_choices, max_length=1)
    q9 = models.CharField(choices=mul_choices, max_length=1)
    name = models.CharField(default="name", max_length=32)