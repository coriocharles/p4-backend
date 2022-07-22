from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static
from .views import CustomTokenObtainPairView

urlpatterns = (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)) + [
    path('admin/', admin.site.urls),
    path('api/', include('tune_app.urls')),
    path('api-auth/', include ('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', include('users.urls', namespace='users'))

]
