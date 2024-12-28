from .views import *
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



urlpatterns = [
    path('api/login/', UserLoginAPIView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/register/', UserRegisterAPIView.as_view(), name='user_registration'),
    path('api/user_profile/', UserProfile.as_view(), name='user_profile'),
    path('api/user_profile/<int:user_id>/', UserProfile.as_view(), name='user_profile_detail'),  # Profile by user ID
    path('api/user/addresses/', GetAddresses.as_view(), name='user_addresses'),
    path('api/user/players/', PlayerApi.as_view(), name='players'),
    path('api/user/teams/', UserTeamApi.as_view(), name='user_teams'),
    path('api/user/question/', QuestionApi.as_view(), name='user_question'),
    path('api/user/teams/<int:user_id>/', UserTeamApi.as_view(), name='user_teams_by_user'),
]