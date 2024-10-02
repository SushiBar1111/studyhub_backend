from rest_framework import generics, permissions
from .models import Convo, Message, Convo
from .serializer import ConvoSerializer, MessageSerializer
from Profile.models import UserProfile
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import base64

class ConvoListCreateView(generics.ListCreateAPIView):
    serializer_class = ConvoSerializer
    permission_classes = []

    def get(self, request):
        user_id = request.query_params.get('id')
        convos = Convo.objects.filter(user1_id=user_id) | Convo.objects.filter(user2_id=user_id)
    
        if not convos.exists():
            return Response({'message': 'No conversations found'}, status=status.HTTP_404_NOT_FOUND)
        convo_list = []
        for convo in convos:
            # buat nentuin current user itu, dia di db convo, di convo nya itu dia user 1 atau user 2
            if convo.user1.id == int(user_id):
                other_user = convo.user2
            else:
                other_user = convo.user1

            # ambil profile yang sesuai dengan id si other_user di atas
            profile = UserProfile.objects.get(id=other_user.id)
            last_message = convo.messages.order_by('-timestamp').first()
            last_message_text = last_message.text.encode('utf-8', 'ignore').decode('utf-8') if last_message else 'No messages yet'

            # Cek apakah profile memiliki profilePicture
            if profile.profilePicture and hasattr(profile.profilePicture, 'file'):
                profile_picture_data = base64.b64encode(profile.profilePicture.file.read()).decode('utf-8')
            else:
                # Jika tidak ada, berikan gambar default (misalnya gambar base64 dari file default)
                profile_picture_data = ''  # Bisa diisi dengan gambar base64 default atau dikosongkan
            
            print(f'Convo ID: {convo.id}, User: {other_user.first_name}, Last Message: {last_message_text}')

            # dictionary dari setiap percakapan (ini list percakapannya)
            convo_data = {
                'convo_id': convo.id,
                'first_name': profile.first_name,
                'profilePicture': profile_picture_data,
                'last_message': {
                    'text': last_message_text,
                    'timestamp': last_message.timestamp if last_message else None
                }
            }

            convo_list.append(convo_data)
        return Response(convo_list, status=status.HTTP_200_OK)
        
class MessageCreateView(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Tidak perlu menambahkan convo_id secara manual
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
        

