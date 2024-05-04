from .serializer import UserPreferenceSerializer
from rest_framework.decorators import api_view
from .models import UserPreference
from django.http import JsonResponse

@api_view(['GET', 'POST'])

def filtering(request):
    if request.method == 'POST':
        serializer = UserPreferenceSerializer(
            data=request.data,
            many=True,
            context = {'request': request}
            )
        if serializer.is_valid():
            user = request.user.profile
            
            existUserPreference = UserPreference.objects.filter(user=user)
            if existUserPreference.exist():
                existUserPreference.delete()
            serializer.save(user=user)
    
    if request.method == 'GET':
        allData = UserPreference.objects.all()
        serializer = UserPreferenceSerializer(allData, many=True)
        return JsonResponse(serializer.data, safe=False)

    
