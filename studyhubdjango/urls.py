from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    path('login/', include('login.urls')),
    path('interest/', include('userInterest.urls')),
    path('filter/', include('filter.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
