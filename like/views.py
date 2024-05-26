from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserLike
from .serializer import LikeSerializer
from rest_framework import status
from Profile.models import UserProfile
from .serializer import UserLikeListSerializer

class Like(APIView): # view buat ngatur user pas like user lain
    permission_classes = [] # ga ada jd bisa login user nya pertama kali
    authentication_classes = [] # ga ada jd bisa login user nya pertama kali
    def post(self, request):
        serializer = LikeSerializer(data=request.data)

        if serializer.is_valid():
            from_user_id = serializer.validated_data['from_user'] # id dari user yg ngelike
            to_user_id = serializer.validated_data['to_user'] # id dari user yang di like
            like, created = UserLike.objects.get_or_create(from_user=from_user_id, to_user=to_user_id) # buat data yg berisi ID user ngelike sm user yang di like

            if created:
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
class UserLikeList(APIView): # view buat list siapa yg like kita
    permission_classes = []
    authentication_classes = []
    def post(self, request):
        id = request.data.get('id')
        filter_user = UserLike.objects.filter(to_user=id).prefetch_related('from_user') # ngefilter data yg ada id si user yg di like aja

        user_data_list = [] # buat nampung list user data yg nge-like
        for every_user in filter_user:
            id_from_user = every_user.from_user.id
            profile = UserProfile.objects.get(id=id_from_user)
            user_data = {
                "first_name": profile.first_name,
                "gender": profile.gender,
                "location": profile.location,
                "role": profile.role,
                "bio": profile.bio,
                "learningType": profile.learningType,
                "studyPlace": profile.studyPlace,
                "academicLevel": profile.academicLevel
            }
            user_data_list.append(user_data)
        serialzer = UserLikeListSerializer(data=user_data_list, many=True)
        if serialzer.is_valid():
            return Response(serialzer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            

