from django.urls import path
from .views import filtering

urlpatterns = [
    path('', filtering.as_view(), name='filter'),
]
