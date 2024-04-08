from rest_framework.decorators import api_view
from data.Profile.models import UserProfile
from django.http import JsonResponse
from .serializer import AllUserSerializer

@api_view(['GET'])
class UsersData(request):
    if request.method == 'GET':
        AllUserData = UserProfile.objects.all()
        serializer = AllUserSerializer(AllUserData, many=True)
        return JsonResponse(serializer.data, safe=False)

