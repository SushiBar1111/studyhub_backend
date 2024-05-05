from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserProfileSerializer
from django.contrib.auth.hashers import make_password

class UserRegister(APIView):
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password'] 
            hashPassword = make_password(password) #hash password
            serializer.validated_data['password'] = hashPassword
            serializer.save() # create dan save user
            return Response(serializer.data, status=status.HTTP_201_CREATED) # user created
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # serializer/form ga valid

   
