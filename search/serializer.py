from rest_framework import serializers
from Profile.models import UserProfile
import base64

class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name',  'gender', 'location', 'role', 'bio', 'learningType', 'studyPlace', 'academicLevel', 'profilePicture']
    def getProfilePicture(self, obj):
        if obj.profilePicture:
            return base64.b64encode(obj.profilePicture.file.read()).decode('utf-8')
        return None