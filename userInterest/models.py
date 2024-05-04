from django.db import models
from Profile.models import UserProfile
from interest.models import Matkul

class UserInterest(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    interest = models.ForeignKey(Matkul, on_delete=models.CASCADE)

    
