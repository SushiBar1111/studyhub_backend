from rest_framework import serializers
from .models import UserInterest

class UserInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInterest
        fields = ['interest']

class ListInterest(serializers.ListSerializer): # class buat list interest biar user bs mlh >1 interest
    child = UserInterestSerializer()

    def createList(self, validated_data):
        user = self.context['request'].user.profile
        interests = [UserInterest(user=user, **item) for item in validated_data]
        return UserInterest.objects.bulk_create(interests)
