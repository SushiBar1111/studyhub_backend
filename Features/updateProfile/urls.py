from django.urls import path
from .views import UpdateProfile

urlpatterns = [
    path('update/', UpdateProfile, name='update'),
]
