from django.db import models
from Profile.models import UserProfile

class Convo(models.Model): # buat naro user mana aja yg punya convo ini
    user1 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='convo_user1')
    user2 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='convo_user2')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"Conversation between {self.user1} and {self.user2}"

class Message(models.Model): # model buat message
     Convo = models.ForeignKey(Convo, on_delete=models.CASCADE, related_name='messages')
     sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
     text = models.TextField()
     timestamp = models.DateTimeField(auto_now_add=True, null=True)

     def __str__(self):
          return f"Message from {self.sender} in conversation {self.Convo}"
