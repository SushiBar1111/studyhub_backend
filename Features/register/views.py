from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from django.contrib.auth.hashers import make_password
from rest_framework import status

@api_view(['POST'])
def UserRegister(request):
    if request.method == 'POST':
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            beforeHashPassword = serializer.validated_data['password']
            hashedPassword = make_password(beforeHashPassword)
            serializer.validated_data['password'] = hashedPassword
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status = 400)