from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Profile.models import UserProfile
from .serializer import UserProfileSerializer


class UserRegister(APIView):
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() #pake DRF password hash automatis
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
