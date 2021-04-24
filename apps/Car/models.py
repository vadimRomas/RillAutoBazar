from django.db import models

# Create your models here.


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
    # user =