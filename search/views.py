from rest_framework.views import APIView
from Profile.models import UserProfile
from django.http import JsonResponse
from .serializer import AllUserSerializer

class UsersData(APIView):
    permission_classes = [] # ga ada jd bisa login user nya pertama kali
    authentication_classes = [] # ga ada jd bisa login user nya pertama kali
    def get(self, request):
        AllUserData = UserProfile.objects.all()
        serializer = AllUserSerializer(AllUserData, many=True)
        return JsonResponse(serializer.data, safe=False)

