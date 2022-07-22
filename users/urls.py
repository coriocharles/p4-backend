from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView, UserDetail, UserList

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('<int:pk>', UserDetail.as_view(), name='UserDetail'),
    path('', UserList.as_view(), name='UserList'),
]
