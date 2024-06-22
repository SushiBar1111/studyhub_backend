from django.urls import path
from .views import Like, UserLikeList, Match

urlpatterns = [
    path('', Like.as_view(), name='like'),
    path('liked-you/', UserLikeList.as_view(), name='like_you'),
    path('decision/', Match.as_view(), name='match')
]