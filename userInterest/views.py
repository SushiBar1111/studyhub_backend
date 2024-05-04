from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ListInterest


def choosingInterest(APIView):
    serializer = UserInterestListSerializer(
        data=request.data,
        many=True,
        context={'request': request}
    )
    if serializer.is_valid:
        user = request.user.profile

        existUserInterest = UserInterest.objects.filter(user=user) #cek user udh prnh pny interest blm
        if existUserInterest.exists():
            existUserInterest.delete() # delete yg udh ada nnti dibuat lg
            serializer.save()
            return Response(status=201)
        else: # klo ga exist ya lgsg save aja serializernya
            serializer.save()
            return Response(status=201)
    else:
        return Response(status=400)
        
