from rest_framework import serializers
from .models import Island, Comment, Media
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'media_type', 'media_url']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    media = MediaSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment_text', 'media']

class IslandSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Island
        fields = ['id', 'longitude', 'latitude', 'area', 'detected_time', 'comments']
