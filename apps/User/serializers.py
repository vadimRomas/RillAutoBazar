from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from apps.UserProfile.serializers import UserProfileSerializer

UserModel = get_user_model()


class UserSerializers(ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = UserModel
        fields = ['name', 'surname', 'email', 'create_date', 'id', 'profile']
