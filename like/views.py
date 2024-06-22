from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserLike
from .serializer import LikeSerializer
from rest_framework import status
from Profile.models import UserProfile
from .serializer import UserLikeListSerializer
from message.models import Convo
from Profile.models import UserProfile

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
        filter_user = UserLike.objects.filter(to_user=id)# ngefilter data yg ada id si user yg di like aja

        if not filter_user.exists():  # ga ada yang suka dia
            return Response({"error": "No users found who liked this user."}, status=status.HTTP_404_NOT_FOUND)
        user_data_list = [] # buat nampung list user data yg nge-like
        for every_user in filter_user: # iterasi user yang nge-like current user
            id_from_user = every_user.from_user.id # ngambil user ID yang nge-like current user
            profile = UserProfile.objects.get(id=id_from_user)
            user_data = {
                'id': profile.pk,
                'first_name': profile.first_name,
                'gender': profile.gender,
                'location': profile.location,
                'role': profile.role,
                'bio': profile.bio,
                'learningType': profile.learningType,
                'studyPlace': profile.studyPlace,
                'academicLevel': profile.academicLevel,
                'profilePicture': profile.profilePicture
            }
            user_data_list.append(user_data)
        listSerializers = []
        for user_data in user_data_list:
            serializer = UserLikeListSerializer(instance=user_data)
            listSerializers.append(serializer)
        
        return Response([serializer.data for serializer in listSerializers], status=status.HTTP_200_OK)

class Match(APIView): #buat handle klo user pilih match atau ngga
    permission_classes = []
    authentication_classes = []
    def post(self, request):

        pilihan = request.data.get('match') # ambil pilihan user match atau ngga
        from_user= request.data.get('from_user') # id dari user yg ngelike
        to_user = request.data.get('to_user') # id dari user yang di like 

        fromUser = UserProfile.objects.get(pk=from_user)
        toUser = UserProfile.objects.get(pk=to_user)
        
        if pilihan == 'Not Match':
            UserLike.objects.filter(from_user_id=from_user, to_user_id=to_user).delete() # kalo ga match entry di like database di apus
            return Response({'message': 'Unmatch'}, status=status.HTTP_200_OK)
        elif pilihan == 'Match': # klo match buat entry baru di table convo + buat table baru buat nampung message jadi bisa chatan
            conversation, created = Convo.objects.get_or_create(user1=fromUser, user2=toUser) # create table convo buat nampung 2 ID user yang match
            UserLike.objects.filter(from_user_id=from_user, to_user_id=to_user).delete() # delete entry
            return Response({'message': 'Matched! Now text your match!'}, status=status.HTTP_201_CREATED)
            

