from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    path('login/', include('login.urls')),
    path('interest/', include('userInterest.urls')),
    path('filter/', include('filter.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('search/', include('search.urls')),
    path('updateProfile/', include('updateProfile.urls')),
    path('profile/', include('Profile.urls'))
]

if settings.DEBUG: # buat saat development aja nanti pas mau deployment diganti ke path sesuai server yg digunain.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)