from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from message.views import MessageCreateView, MessageListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    path('login/', include('login.urls')),
    path('interest/', include('userInterest.urls')),
    path('filter/', include('filter.urls')),
    path('search/', include('search.urls')),
    path('updateProfile/', include('updateProfile.urls')),
    path('profile/', include('Profile.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/validate/', include('api.urls')),
    path('like/', include('like.urls')),
    path('profileImage/', include('updateProfile.urls')),
    path('liked/', include('like.urls')),
    path('match/', include('like.urls')),
    path('convo/', include('message.urls')),
    path('message/', MessageCreateView.as_view(), name='create_message'),
    path('message/list/', MessageListView.as_view(), name='message_list'),
    path('getConvoId/', include('message.urls'))
]

if settings.DEBUG: # buat saat development aja nanti pas mau deployment diganti ke path sesuai server yg digunain.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)