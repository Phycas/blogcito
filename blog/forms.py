from django import forms
from .models import Post

class post_crea_form(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'slug', 'description', 'content', 'published', )