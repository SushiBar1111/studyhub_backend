from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import InterestSerializer
from .serializer import UserInterestSerializer
from Profile.models import UserProfile
from .models import UserInterest
from interest.models import Matkul

class choosingInterest(APIView):
    permission_classes = [] # ga ada jd bisa login user nya pertama kali
    authentication_classes = [] # ga ada jd bisa login user nya pertama kali
    def post(self, request):

        serializer = UserInterestSerializer(data=request.data)

        if serializer.is_valid:
            user_id = serializer.validated_data['id'] # akses user ID dr serializer
            user_profile = UserProfile.objects.get(id=user_id) # get user profile berdasarkan ID

            UserInterest.objects.filter(user=user_profile).delete() # delete existing user interest
            
            for interest_item in serializer.data['interest']:
                interest_serializer = InterestSerializer(data=serializer.data['interest'])
                
                try:
                    interest, created = Matkul.objects.get_or_create(interest=serializer.data['matkul'])
                    UserInterest.objects.create(user=user_profile, interest=interest)
                except Matkul.DoesNotExist:
                    continue
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
