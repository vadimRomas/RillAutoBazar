from rest_framework.serializers import ModelSerializer

from .models import UsersProfileModel


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UsersProfileModel
        fields = ['father_name', 'age', 'region', 'city', 'avatar', 'id']
