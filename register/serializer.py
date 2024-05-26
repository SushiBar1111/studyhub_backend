from rest_framework import serializers
from Profile.models import UserProfile
from rest_framework.exceptions import ValidationError
import re
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['email', 'password', 'birth_date']
        extra_kwargs = {
            'password' : {'write_only': True} #biar ga muncul di response klo ntar responsenya mau diganti jd munculin username
        }
    def EmailValidate(self, value):
        if UserProfile.objects.filter(email=value).exists():
            raise ValidationError('Email has already been used')

    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("Password must be at least 8 characters long")
        if not re.search(r'[A-Z]', value):
            raise ValidationError("Password must contain at least one uppercase letter")
        if not re.search(r'\d', value):
            raise ValidationError("Password must contain at least one digit")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise ValidationError("Password must contain at least one special character")
        return value
        
       

        
   

   