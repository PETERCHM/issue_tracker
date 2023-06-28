from django import forms
from .models import Issue, Comment

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'status', 'priority', 'assigned_user']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'author']
        