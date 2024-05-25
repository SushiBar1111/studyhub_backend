from rest_framework import serializers
from Profile.models import UserProfile

class updateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        extra_kwargs = {'id':{'read_only':True}, # extra kwargs ini buat validasi serializer biar user ga harus update semua data mereka sekaligus
                        'email':{'required':False, 'allow_blank':True},
                        'first_name':{'required':False, 'allow_blank':True},
                        'last_name':{'required':False, 'allow_blank':True},
                        'gender':{'required':False, 'allow_blank':True},
                        'location':{'required':False, 'allow_blank':True},
                        'role':{'required':False, 'allow_blank':True},
                        'bio':{'required':False, 'allow_blank':True},
                        'academicLevel':{'required':False, 'allow_blank':True},
                        'studyPlace':{'required':False, 'allow_blank':True},
                        'learningType':{'required':False, 'allow_blank':True},
                        }
        fields = [ 'id','email','first_name', 'last_name', 'gender', 'location', 'role', 'bio', 'academicLevel', 'studyPlace', 'learningType']