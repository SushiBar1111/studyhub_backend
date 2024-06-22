from rest_framework import serializers
from .models import UserLike
from Profile.models import UserProfile
import base64
class LikeSerializer(serializers.ModelSerializer): # serializer buat ngambil like dari user
    class Meta:
        model = UserLike
        fields = ['from_user', 'to_user']


class UserLikeListSerializer(serializers.ModelSerializer): # serializer buat user bisa tau siapa yg like dia
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name',  'gender', 'location', 'role', 'bio', 'learningType', 'studyPlace', 'academicLevel', 'profilePicture']
    def getProfilePicture(self, obj):
        if obj.profilePicture:
            return base64.b64encode(obj.profilePicture.file.read()).decode('utf-8')
        return None

