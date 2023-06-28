from django.shortcuts import render
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from .models import Issue, Comment
from .forms import IssueForm, CommentForm

def issue_list(request):
    issues = Issue.objects.all()
    return render(request, 'issue_list.html', {'issues': issues})

def issue_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    comments = issue.comments.all()
    comment_form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.issue = issue
            comment.save()
            return redirect('issue_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'issue_detail.html', {'issue': issue, 'comments': comments, 'comment_form': comment_form})

def issue_create(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save()
            return redirect('issue_detail', pk=issue.pk)
    else:
        form = IssueForm()
    return render(request, 'issue_create.html', {'form': form})


def add_comment(request, pk):
    issue = get_object_or_404(Issue, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.issue = issue
            comment.save()
            return redirect('issue_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form': form})

def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('issue_detail', pk=comment.issue.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'edit_comment.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect
from .models import Comment

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('issue_detail', pk=comment.issue.pk)

    return render(request, 'delete_comment.html', {'comment': comment})
