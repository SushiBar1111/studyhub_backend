from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Profile.models import UserProfile
from .serializer import updateProfileSerializer
from rest_framework.permissions import IsAuthenticated

class UpdateProfile(APIView):
    

    def patch(self, request):
        
        id = request.data.get('id') # ngambil ID dari user yg request
        try:
            user = UserProfile.objects.get(id=id)
        except UserProfile.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = updateProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Profile updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)