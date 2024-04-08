from django.urls import path
from .views import choosingInterest

urlpatterns = [
    path('interest/', choosingInterest, name='interest'),
]
