from rest_framework import serializers
from .models import UserPreference

class UserPreferenceSerializer(serializers.ModelSerializer):
    model = UserPreference
    fields = ['id', 'preferences']