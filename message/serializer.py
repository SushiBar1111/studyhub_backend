from rest_framework import serializers
from .models import Convo, Message
from Profile.models import UserProfile

class ConvoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convo
        fields = ['id', 'user1', 'user2', 'created_at', 'messages']

class MessageSerializer(serializers.ModelSerializer):
    convo = ConvoSerializer(read_only=True)
    sender = serializers.StringRelatedField()
    class Meta:
        model = Message
        fields = ['Convo_id', 'convo', 'sender', 'text', 'timestamp']

class ChatListSerializer(serializers.ModelSerializer): # cuman buat serializer chat list
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'profilePicture']

