from rest_framework import serializers
from .models import UserProfile
import base64
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [ 'first_name', 'email', 'gender', 'matkul', 'location', 'role', 'bio', 'learningType', 'studyPlace', 'academicLevel', 'profilePicture']
    def getProfilePicture(self, obj):
        if obj.profilePicture:
            return base64.b64encode(obj.profilePicture.file.read()).decode('utf-8')
        return None