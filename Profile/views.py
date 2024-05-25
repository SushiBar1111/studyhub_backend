from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProfileSerializer
from Profile.models import UserProfile

class UserProfileView(APIView):
    def get(self, request):
        user_id = request.query_params.get('id')  # mendapatkan ID dari query parameter

        if not user_id:
            return Response({"error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_profile = UserProfile.objects.get(id=user_id)  # mengambil user yang sesuai ID
        except UserProfile.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)