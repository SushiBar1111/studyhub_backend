from rest_framework import serializers
from data.Profile.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['email', 'password', 'first_name', 'last_name', 'gender', 'age', 'location', 'role']
    
    def EmailValidate(self, value):
        if UserProfile.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email has already been used')
        return value