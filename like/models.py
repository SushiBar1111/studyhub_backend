from django.db import models
from Profile.models import UserProfile

class UserLike(models.Model):
    from_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='likes_sent') # user yg like
    to_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='likes_received') # user yg di like
    created_at = models.DateTimeField(auto_now_add=True)
