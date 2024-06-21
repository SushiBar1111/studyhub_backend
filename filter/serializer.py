from rest_framework import serializers
from .models import UserPreference
from preference.models import Preference
from Profile.models import UserProfile
class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        extra_kwargs = {
                        'gender':{'required':False, 'allow_blank':True},
                        'matkul':{'required':False, 'allow_blank':True},
                        'role':{'required':False, 'allow_blank':True},
                        'academicLevel':{'required':False, 'allow_blank':True},
                        'studyPlace':{'required':False, 'allow_blank':True},
                        'learningType':{'required':False, 'allow_blank':True},
                        'learningType':{'required':False, 'allow_blank':True},
                        }
        fields = [ 'gender', 'matkul', 'role', 'academicLevel', 'studyPlace', 'learningType']
class UserPreferenceSerializer(serializers.ModelSerializer):
    preferences = PreferenceSerializer(many=True)
    id = serializers.IntegerField()
    class Meta:
        model = UserPreference
        fields = ['id','preferences']