from .serializer import UserPreferenceSerializer
from rest_framework.views import APIView
from .models import UserPreference
from rest_framework.response import Response
from preference.models import Preference
from rest_framework import status
from Profile.models import UserProfile

class filtering(APIView):
    permission_classes = [] # ga ada jd bisa login user nya pertama kali
    authentication_classes = [] # ga ada jd bisa login user nya pertama kali
    def post(self, request):
        serializer = UserPreferenceSerializer(data=request.data)

        if serializer.is_valid():
            user_id = serializer.validated_data['id']  # Access user ID from serializer
            user_profile = UserProfile.objects.get(id=user_id)  # Get user profile

            UserPreference.objects.filter(user=user_profile).delete()  # Delete existing preferences for this user

            for preference_item in serializer.data['preferences']:
                gender = preference_item.get('gender')
                role = preference_item.get('role')
                academicLevel = preference_item.get('academicLevel')
                location = preference_item.get('location')
                studyPlace = preference_item.get('studyPlace')
                learningType = preference_item.get('learningType')
                matkul = preference_item.get('matkul')

                try:
                    preference, created = Preference.objects.get_or_create(  # Check for existing preference
                        gender=gender,
                        role=role,
                        academicLevel=academicLevel,
                        location=location,
                        studyPlace=studyPlace,
                        learningType=learningType,
                        matkul=matkul
                    )
                    UserPreference.objects.create(user=user_profile, preferences=preference)  # Create user preference
                except Preference.DoesNotExist:
                    continue

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)