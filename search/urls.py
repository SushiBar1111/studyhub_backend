from django.urls import path
from .views import UsersData

urlpatterns = [
    path('', UsersData.as_view(), name='search'),
]
