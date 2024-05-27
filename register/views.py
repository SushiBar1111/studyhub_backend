from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserProfileSerializer
from django.contrib.auth.hashers import make_password


class UserRegister(APIView):
    permission_classes = [] # ga ada jd bisa login user nya pertama kali
    authentication_classes = [] # ga ada jd bisa login user nya pertama kali
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password'] 
            hashPassword = make_password(password) #hash password
            serializer.validated_data['password'] = hashPassword
            serializer.save() # create dan save user
            user_id = serializer.instance.id
            return Response({'id': user_id}, status=status.HTTP_201_CREATED) # user created
        else:
            return Response({"Email already exists"}, status=status.HTTP_400_BAD_REQUEST)

   
