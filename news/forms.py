from datetime import datetime 
from django import forms
from .models import NewsArticle

class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = "__all__"

        widgets = {"title" : forms.TextInput(attrs = {"placeholder" : "tuliskan judul"}),
                "content" : forms.Textarea(attrs = {"rows" : 3, "placeholder" : "tuliskan isi"})}