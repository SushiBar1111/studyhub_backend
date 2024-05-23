from rest_framework.views import APIView
from .serializer import updateProfileSerializer
from rest_framework.response import Response
from Profile.models import UserProfile

class UpdateProfile(APIView):
    def patch(self, request):
        user = request.user
        profile = user.profile
        
        serializer = updateProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        return Response(status=400)
