from rest_framework import serializers
from Profile.models import UserProfile
import re
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['email', 'password', 'first_name', 'last_name', 'gender', 'birth_date', 'location', 'role']
        extra_kwargs = {
            'password' : {'write_only': True} #biar ga muncul di response klo ntar responsenya mau diganti jd munculin username
        }
    
    def EmailValidate(self, value):
        if UserProfile.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email has already been used')
        return value

    def PasswordValidate(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long.')
        if not re.search(r'[A-Z]', value): #validate uppercase
            raise serializer.ValidationError('Password must contain at least one UPPERCASE')
        if not re.search(r'[0-9]', value): #validate number
            raise serializer.ValidationError('Password must contain at least one NUMBER DIGIT')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value): #validate special character
            raise serializer.ValidationError('Password must contain at least one SPECIAL CHARACTER')
        