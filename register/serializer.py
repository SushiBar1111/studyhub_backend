from rest_framework import serializers
from Profile.models import UserProfile
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['email', 'password', 'first_name', 'last_name', 'gender', 'location', 'role', 'birth_date']
        extra_kwargs = {
            'password' : {'write_only': True} #biar ga muncul di response klo ntar responsenya mau diganti jd munculin username
        }
    def EmailValidate(self, value):
        if UserProfile.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email has already been used')
        return value
            
        
       

        
   

   