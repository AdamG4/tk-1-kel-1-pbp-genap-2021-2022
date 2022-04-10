from django import forms
from .models import ForumPost

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'content']

        widgets = {"title" : forms.TextInput(attrs = {"placeholder" : "tuliskan judul"}),
                "content" : forms.Textarea(attrs = {"rows" : 3, "placeholder" : "tuliskan isi"})}