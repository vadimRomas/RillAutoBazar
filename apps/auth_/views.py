from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from apps.auth_.serializers import RegisterSerializers

UserModel = get_user_model()


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializers
    permission_classes = [AllowAny]
    queryset = UserModel.objects.all()
