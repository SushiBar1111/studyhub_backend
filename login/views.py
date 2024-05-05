from rest_framework.views import APIView
from .serializer import UserLoginSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from Profile.models import UserProfile


class UserLogin(APIView):
    def post(self, request):
        user = get_object_or_404(UserProfile, email=request.data['email']) # fetch data dari UserProfile buat disamain sm request data
        if not user.check_password(request.data['password']): # cek password berdasarkan email
            return Response({'message': 'Invalid Credentials'},status=401)
        serializer = UserLoginSerializer(instance=user)
        return Response({'message': 'Login Success'})




