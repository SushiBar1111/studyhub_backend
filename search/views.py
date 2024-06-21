from rest_framework.views import APIView
from Profile.models import UserProfile
from django.http import JsonResponse
from .serializer import AllUserSerializer
from rest_framework import status
class UsersData(APIView):
    permission_classes = [] # ga ada jd bisa login user nya pertama kali
    authentication_classes = [] # ga ada jd bisa login user nya pertama kali
    def post(self, request):
        id = request.data.get('id') #ngambil id si user
        AllUserData = UserProfile.objects.exclude(id=id) # mengambil semua user data kecuali data si pemilik ID
        serializer = AllUserSerializer(AllUserData, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

