from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Profile.models import UserProfile
from .serializer import updateProfileSerializer, profilePictureSerializer

class UploadImage(APIView):
    def post(self, request):
        serializer = profilePictureSerializer(data=request.data)
        id = request.data.get('id')
        if serializer.is_valid():
            try:
                user = UserProfile.objects.get(id=id)
                user.profilePicture = request.data['profilePicture']
                user.save()
                return Response({'message': 'Profile picture uploaded successfully.'}, status=status.HTTP_200_OK)
            except UserProfile.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdateProfile(APIView):
    permission_classes = [] # ga ada jd bisa login user nya pertama kali
    authentication_classes = [] # ga ada jd bisa login user nya pertama kali
    def patch(self, request):
        
        id = request.data.get('id') # ngambil ID dari user yg request
        try:
            user = UserProfile.objects.get(id=id)
        except UserProfile.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = updateProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            if 'profilePicture' in request.FILES:
                user.profilePicture = request.FILES['profilePicture']
            serializer.save()
            return Response({'message': 'Profile updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)