from rest_framework.views import APIView
from Profile.models import UserProfile
from django.http import JsonResponse
from .serializer import AllUserSerializer

class UsersData(APIView):
    if request.method == 'GET':
        AllUserData = UserProfile.objects.all()
        serializer = AllUserSerializer(AllUserData, many=True)
        return JsonResponse(serializer.data, safe=False)

