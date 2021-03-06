# Generated by Django 3.2.3 on 2021-06-11 09:57

import apps.UserProfile.services
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(150)])),
                ('father_name', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('avatar', models.ImageField(upload_to=apps.UserProfile.services.avatar_upload)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'users_profile',
            },
        ),
    ]
