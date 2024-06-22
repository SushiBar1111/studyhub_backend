from django.urls import path
from .views import UpdateProfile, UploadImage

urlpatterns = [
    path('', UpdateProfile.as_view(), name='update'),
    path('upload/', UploadImage.as_view(), name='image'),
]
