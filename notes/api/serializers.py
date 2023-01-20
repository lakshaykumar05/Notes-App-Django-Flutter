from rest_framework.serializers import ModelSerializer
from .models import Note
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
