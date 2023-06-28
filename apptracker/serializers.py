from rest_framework import serializers
from .models import Issue, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'issue', 'content', 'created_at', 'updated_at')

class IssueSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Issue
        fields = ('id', 'title', 'description', 'created_at', 'updated_at', 'comments')
