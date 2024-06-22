from rest_framework import generics, permissions
from .models import Convo, Message, Convo
from .serializer import ConvoSerializer, MessageSerializer, ChatListSerializer
from Profile.models import UserProfile
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class ConvoListCreateView(generics.ListCreateAPIView):
    serializer_class = ConvoSerializer
    permission_classes = []

    def get(self, request):
        user_id = request.query_params.get('id')
        convos = Convo.objects.filter(user1_id=user_id) | Convo.objects.filter(user2_id=user_id)
    
        if not convos.exists():
            return Response({'message': 'No conversations found'}, status=status.HTTP_404_NOT_FOUND)
        convo_list = []
        for every_user in convos: # iterasi user yang nge-like current user
            id_from_user = every_user.user1.id | every_user.user2.id # ngambil user ID yang nge-like current user
            profile = UserProfile.objects.get(id=id_from_user)
            user_data = {
                'id': profile.pk,
                'first_name': profile.first_name,
                'profilePicture': profile.profilePicture
            }
            convo_list.append(user_data)
        listSerializers = []
        for user_data in convo_list:
            serializer = ChatListSerializer(instance=user_data)
            listSerializers.append(serializer)
        print(listSerializers)
        return Response([serializer.data for serializer in listSerializers], status=status.HTTP_200_OK)
        
class MessageCreateView(APIView):
    def post(self, request):
        convo_id = request.user.convo_id  # Assuming the user has a convo_id attribute
        serializer = MessageSerializer(data=request.data)
        serializer.validated_data['Convo_id'] = convo_id
        if serializer.is_valid():
            serializer.save()
            return Response("message sent", status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class MessageListView(APIView):
    def get(self, request):
        convo_id = request.query_params.get('convo_id')
        messages = Message.objects.filter(convo_id=convo_id).order_by('-timestamp')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    

class GetConvoId(APIView):
    def post(self, request):
        user1 = request.data.get('user1')
        user2 = request.data.get('user2')
        convo = Convo.objects.filter(user1_id=user1, user2_id=user2)
        if not convo.exists():
            return Response({'convo_id': convo}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'error ngab'}, status=status.HTTP_200_OK)
        

