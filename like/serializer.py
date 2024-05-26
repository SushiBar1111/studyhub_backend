from rest_framework import serializers
from .models import UserLike
from Profile.models import UserProfile
class LikeSerializer(serializers.ModelSerializer): # serializer buat ngambil like dari user
    class Meta:
        model = UserLike
        fields = ['from_user', 'to_user']


class UserLikeListSerializer(serializers.ModelSerializer): # serializer buat user bisa tau siapa yg like dia
    class Meta:
        model = UserProfile
        fields = [ 'first_name', 'gender', 'location', 'role', 'bio', 'learningType', 'studyPlace', 'academicLevel']


