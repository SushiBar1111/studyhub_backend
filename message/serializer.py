from rest_framework import serializers
from .models import Convo, Message
from Profile.models import UserProfile

class ConvoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convo
        fields = ['id', 'user1', 'user2', 'created_at', 'messages']

class MessageSerializer(serializers.ModelSerializer):
    convo = serializers.PrimaryKeyRelatedField(queryset=Convo.objects.all())  # Relasi ke convo
    sender = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())  # Relasi ke sender

    class Meta:
        model = Message
        fields = ['convo', 'sender', 'text', 'timestamp']  # Sertakan 'sender' di dalam fields





