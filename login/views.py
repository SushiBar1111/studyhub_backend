from rest_framework.views import APIView
from rest_framework.response import Response
from Profile.models import UserProfile
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
class UserLogin(APIView):
    permission_classes = [] # ga ada jd bisa login user nya pertama kali
    authentication_classes = [] # ga ada jd bisa login user nya pertama kali
    def post(self, request):
    
        email = request.data['email']
        password = request.data['password']

        user = UserProfile.objects.filter(email=email).first()

        if user is None:
            return Response({'Invalid Credentials'})#klo ga ada user pake email tersebut
        
        if not user.check_password(password): # cek password berdasarkan email
            return Response({'Invalid Credentials'})
        
        refresh = RefreshToken.for_user(user) #buat token JWT
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    
        
        




