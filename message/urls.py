from django.urls import path
from .views import ConvoListCreateView, MessageCreateView, MessageListView, GetConvoId

urlpatterns = [
    path('list/', ConvoListCreateView.as_view(), name='ConvoList'),
    path('', GetConvoId.as_view(), name='convo_id'),
]