from rest_framework import serializers
from .models import UserProfile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [ 'first_name', 'email', 'gender', 'matkul', 'location', 'role', 'bio', 'learningType', 'studyPlace', 'academicLevel']