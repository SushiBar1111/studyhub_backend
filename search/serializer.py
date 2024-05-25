from rest_framework import serializers
from Profile.models import UserProfile


class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [ 'first_name', 'last_name', 'gender', 'location', 'role', 'bio', 'learningType', 'studyPlace', 'academicLevel']