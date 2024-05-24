from .serializer import UserPreferenceSerializer
from rest_framework.views import APIView
from .models import UserPreference
from rest_framework.response import Response
from preference.models import Preference
from rest_framework import status

class filtering(APIView):
    def post(self, request): # create data di intermediary table untuk preferensi user
        serializer = UserPreferenceSerializer(
            data=request.data,
            many=True,
            context = {'request': request}
            )
       
        if serializer.is_valid():
            id = serializer.data['id']
            user_preference = serializer.data['preferences']
            
            existUserPreference = UserPreference.objects.filter(id=id)# nyari apakah user udh punya preferensi sebelumnya
            if existUserPreference.exist(): 
                existUserPreference.delete()#delete preferensi sebelumnya 
            
            for item_preference in user_preference:
                preference = Preference.objects.create(**item_preference) #create objek data berisi preferensi user
                UserPreference.objects.create(user=id, preferences=preference) #create objek berisi prefensi user dan id user

            return Response(UserPreference, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    
            
    
