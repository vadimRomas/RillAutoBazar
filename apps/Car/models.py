from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from apps.Car.services import images_car_upload

UserModel = get_user_model()


class CarsModel(models.Model):
    class Meta:
        db_table = 'cars'

    type = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    mileage = models.IntegerField()
    region = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    price = models.IntegerField()
    save_cars = models.ManyToManyField(UserModel, related_name='save_cars')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='car')


class ImagesCarModel(models.Model):
    class Meta:
        db_table = 'images_car'
    img = models.ImageField(upload_to=images_car_upload)
    car = models.ForeignKey(CarsModel, on_delete=models.CASCADE, related_name='images')
