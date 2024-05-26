from rest_framework import serializers
from .models import UserInterest
from interest.models import Matkul

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matkul
        fields = ['matkul']

class UserInterestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    interests = serializers.ListField(child=serializers.ChoiceField(choices=Matkul.MATKUL_CHOICES)
    )
