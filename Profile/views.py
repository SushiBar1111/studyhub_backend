from rest_framework import api_view
from .serializer import ProfileSerializer
from django.http import JsonResponse

@api_view(['GET'])
class getProfile(request):
    if request.method == 'GET':
        serializer = ProfileSerializer(data=request.data)
        return JsonResponse(serializer.data, safe=False)
