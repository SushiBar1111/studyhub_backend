from django.db import models
from data.Profile.models import UserProfile
from data.preference.models import Preference

class UserPreference(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    preferences = models.ForeignKey(Preference, on_delete=models.CASCADE)

    