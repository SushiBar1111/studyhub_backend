from rest_framework import serializers
from data.Profile.models import UserProfile


class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [ 'first_name', 'last_name', 'gender', 'age', 'location', 'role']