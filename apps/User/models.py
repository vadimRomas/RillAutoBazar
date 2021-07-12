from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core import validators as v

from apps.User.managers import CustomUserManager
# Create your models here.

class UsersModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'users'
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    create_date = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
