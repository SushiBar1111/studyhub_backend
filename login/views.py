from rest_framework.views import APIView
from .serializer import UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth import login


class UserLogin(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validate_data['password']
            userAuth = authenticate(request, email=email, password=password)
            if userAuth:
                login(request, userAuth)
                return Response(status=200)
            else:
                return Response(status=400)
        else:
            return Response(serializer.errors, status=400)




