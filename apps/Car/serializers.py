from rest_framework.serializers import ModelSerializer

from apps.Car.models import CarsModel, ImagesCarModel
from apps.User.serializers import UserSerializers


class CarSerializer(ModelSerializer):
    user = UserSerializers(read_only=True)

    class Meta:
        model = CarsModel
        fields = ['type', 'brand', 'model', 'year', 'mileage', 'region', 'city', 'price', 'id', 'user']
        extra_kwargs = {
            'user_id': {'read_only': True}
        }


class ImagesCarSerializer(ModelSerializer):

    class Meta:
        model = ImagesCarModel
        fields = ['img']
