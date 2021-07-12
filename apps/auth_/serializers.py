from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, ValidationError

UserModel = get_user_model()


class RegisterSerializers(ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'name', 'surname', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        try:
            user = UserModel.objects.create_user(**validated_data)
        except ValueError as err:
            raise ValidationError(err)
        return user