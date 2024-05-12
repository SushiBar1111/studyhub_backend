from django.urls import path
from .views import UpdateProfile

urlpatterns = [
    path('', UpdateProfile.as_view(), name='update'),
]
