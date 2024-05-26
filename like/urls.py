from django.urls import path
from .views import Like, UserLikeList, Match

urlpatterns = [
    path('', Like.as_view(), name='like'),
    path('like_you/', UserLikeList.as_view(), name='like_you'),
    path('match/', Match.as_view(), name='match')
]