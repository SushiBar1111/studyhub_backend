from rest_framework.views import APIView
from rest_framework.response import Response
from Profile.models import UserProfile
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
class UserLogin(APIView):
    
    def post(self, request):
    
        email = request.data['email']
        password = request.data['password']

        user = UserProfile.objects.filter(email=email).first()

        if user is None:
            return Response({'Invalid Credentials'})#klo ga ada user pake email tersebut
        
        if not user.check_password(password): # cek password berdasarkan email
            return Response({'Invalid Credentials'})
        
        token = Token.objects.create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    
        
        




