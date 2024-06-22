from django.urls import path
from .views import ValidateToken

urlpatterns = [
    path('', ValidateToken.as_view(), name='validate'),
]