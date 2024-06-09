from rest_framework import generics, permissions
from .models import Convo, Message
from .serializer import ConvoSerializer, MessageSerializer
from Profile.models import UserProfile

class ConvoListCreateView(generics.ListCreateAPIView): # view buat nge list convo yg dimiliki oleh user
    serializer_class = ConvoSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        return Convo.objects.filter(user1=user) | Convo.objects.filter(user2=user)

class MessageCreateView(generics.CreateAPIView): # view buat create message 
    serializer_class = MessageSerializer
    permission_classes = []

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class ConvoDetailView(generics.RetrieveAPIView):
    queryset = Convo.objects.all()
    serializer_class = ConvoSerializer
    permission_classes = []
