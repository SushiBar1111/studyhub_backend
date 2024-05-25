from rest_framework import serializers
from .models import UserProfile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [ 'first_name', 'gender', 'location', 'role', 'bio', 'learningType', 'studyPlace', 'academicLevel']