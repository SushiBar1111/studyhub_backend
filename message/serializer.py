from rest_framework import serializers
from .models import Convo, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'convo', 'sender', 'text', 'timestamp']

class ConvoSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Convo
        fields = ['id', 'user1', 'user2', 'created_at', 'messages']
