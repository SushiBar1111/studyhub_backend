from django.urls import path
from .views import UsersData

urlpatterns = [
    path('search/', UsersData, name='search'),
]
