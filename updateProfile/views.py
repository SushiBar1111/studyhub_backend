from rest_framework.decorators import api_view
from .serializer import updateProfileSerializer
from rest_framework.response import Response

@api_view(['POST'])
class UpdateProfile(request):
    if request.method == 'POST':
        serializer = updateProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=200)
