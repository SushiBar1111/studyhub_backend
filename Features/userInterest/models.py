from django.db import models
from data.Profile.models import UserProfile
from data.interest.models import Matkul

class UserInterest(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    interest = models.ForeignKey(Matkul, on_delete=models.CASCADE)

    
