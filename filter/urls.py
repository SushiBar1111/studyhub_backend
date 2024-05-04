from django.urls import path
from .views import filtering

urlpatterns = [
    path('filter/', filtering, name='filter'),
]
