from django.db import models
from django.contrib.auth import get_user_model
from django.core import validators as v

from .services import avatar_upload

UserModel = get_user_model()


# Create your models here.
class UsersProfileModel(models.Model):
    class Meta:
        db_table = 'users_profile'

    age = models.IntegerField(validators=[
        v.MinValueValidator(18),
        v.MaxValueValidator(150)
    ])
    father_name = models.CharField(max_length=60)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=80)
    avatar = models.ImageField(upload_to=avatar_upload)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
