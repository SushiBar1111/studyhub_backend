from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class ValidateToken(APIView):
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        return Response(status=status.HTTP_200_OK)