from rest_framework.decorators import api_view
from .serializer import UserLoginSerializer
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth import login

@api_view(['POST'])
def UserLogin(request):
    if request.method == 'POST':
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




