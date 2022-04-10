from datetime import datetime 
from django import forms
from .models import Score

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['team_1', 'score_1', 'team_2', 'score_2']

        widgets = {"team_1" : forms.TextInput(attrs = {"placeholder" : "team 1"}),
                "score_1" : forms.NumberInput(attrs = {"placeholder" : 0}),
                "team_2" : forms.TextInput(attrs = {"placeholder" : "team 2"}),
                "score_2" : forms.NumberInput(attrs = {"placeholder" : 0})}