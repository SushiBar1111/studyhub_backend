from rest_framework import serializers
from Profile.models import UserProfile

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['email', 'password']
    
    



                

        