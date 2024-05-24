from rest_framework import serializers
from .models import UserPreference
from preference.models import Preference
from Profile.models import UserProfile
class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = '__all__'
class UserPreferenceSerializer(serializers.ModelSerializer):
    preferences = PreferenceSerializer(many=True)
    id = serializers.IntegerField()
    class Meta:
        model = UserPreference
        fields = ['id','preferences']