from rest_framework.views import APIView
from .serializer import updateProfileSerializer
from rest_framework.response import Response

class UpdateProfile(APIView):
    def put(self, request):
        serializer = updateProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        return Response(status=400)
