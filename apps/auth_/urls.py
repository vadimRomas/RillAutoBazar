from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth_.views import RegisterView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='tokens'),
    path('/refresh', TokenRefreshView.as_view(), name='refresh'),
    path('/register', RegisterView.as_view())
]
