from rest_framework.serializers import ModelSerializer

from .models import UsersProfileModel



class UserProfileSerializers(ModelSerializer):
    class Meta:
        model = UsersProfileModel
        fields = []
