from django.urls import path
from .views import choosingInterest

urlpatterns = [
    path('', choosingInterest.as_view(), name='interest'),
]
