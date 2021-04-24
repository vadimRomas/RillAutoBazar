from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core import validators as v

from apps.User.managers import CustomUserManager
from enums.profile_enums import REGEXP_NAME
# Create your models here.

class UsersModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'users'
    name = models.CharField(max_length=50, validators=[
     v.RegexValidator(REGEXP_NAME, 'Тільки українські буквиб мін 2 макс 20 букв')
    ])
    surname = models.CharField(max_length=50, validators=[
        v.RegexValidator(REGEXP_NAME, 'Тільки українські буквиб мін 2 макс 20 букв')
    ])
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    create_date = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
