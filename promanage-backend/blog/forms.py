from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'is_public', 'project', 'tags', 'cover_image']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'rich-text-editor'}),
        }
